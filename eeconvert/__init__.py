import boto3
import botocore
import sqlalchemy
import ee

def rdsConnect(database_identifier,database_name,master_username):
    """open a connection to AWS RDS
    
    in addition to specifying the arguments you need to store your password in a file called .password in the current working directory. 
    You can do this using the command line or Jupyter. Make sure to have your .gitignore file up to date.
    
    Args:
        database_identifier (string) : postgresql database identifier used when you set up the AWS RDS instance
        database_name (string) : the database name to connect to
        master_username (string) : the master username for the database
        
    Returns:
        engine (sqlalchemy.engine.base.Engine) : database engine
        connection (sqlalchemy.engine.base.Connection) : database connection
    """
    
    
    rds = boto3.client('rds')
    F = open(".password","r")
    password = F.read().splitlines()[0]
    F.close()
    response = rds.describe_db_instances(DBInstanceIdentifier="%s"%(database_identifier))
    status = response["DBInstances"][0]["DBInstanceStatus"]
    print("Status:",status)
    endpoint = response["DBInstances"][0]["Endpoint"]["Address"]
    print("Endpoint:",endpoint)
    engine = sqlalchemy.create_engine('postgresql://%s:%s@%s:5432/%s' %(master_username,password,endpoint,database_name))
    connection = engine.connect()
    return engine, connection



def fcToGdf(fc,crs = {'init' :'epsg:4326'}):
    """converts a featurecollection to a geoPandas GeoDataFrame. Use this function only if all features have a geometry.  
    
    caveats:
    Currently only supports non-geodesic (planar) geometries because of limitations in geoPandas and Leaflet. Geodesic geometries are simply interpreted as planar geometries. 
    FeatureCollections larger than memory are currently not supported. Consider splitting data and merging (server side) afterwards. 
    
    Args:
        fc (ee.FeatureCollection) : the earth engine feature collection to convert. 
        crs (dictionary, optional) : the coordinate reference system in geopandas format. Defaults to {'init' :'epsg:4326'}
        
    Returns:
        gdf (geoPandas.GeoDataFrame or pandas.DataFrame) : the corresponding (geo)dataframe. 
        
    """
    crs = {'init' :'epsg:4326'}
    
    features = fc.getInfo()['features']
    dictarr = []

    for f in features:
        #geodesic = ee.Feature(f).geometry().edgesAreGeodesics()
        #if geodesic:
        attr = f['properties']
        attr['geometry'] = f['geometry']
        attr['geometry']
        dictarr.append(attr)

    gdf = gpd.GeoDataFrame(dictarr)
    gdf['geometry'] = map(lambda s: shapely.geometry.shape(s), gdf.geometry)
    gdf.crs = crs
    return gdf




