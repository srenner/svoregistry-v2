import psycopg2
from urllib.request import urlopen
import json
import time
import sys

def main():
    conn_string = "host='localhost' dbname='svoregistry' user='svo' password='" + sys.argv[0] + "'"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute("""select id, trim(concat(city, ' ', state, ' ', zipcode, ' ', country)) as location, geo_lat, geo_long
                        from registry_entry re
                        where ((length(city) > 0) or (length(state) > 0) or (length(zipcode) > 0))
                        and (geo_lat is null and geo_long is null)""")
    entries = cursor.fetchall()
    conn.close()
    totalcount = len(entries)
    successcount = 0
    for entry in entries:
        id = entry[0]
        address = entry[1].replace(' ', '%20')
        
        geocode_url = 'http://maps.googleapis.com/maps/api/geocode/json?address=' + address + '&sensor=false'
        #print geocode_url + '\n'
        handle = urlopen(geocode_url)
        jsonResponse = handle.read().decode("utf-8")
        handle.close()
        
        
        
        objs = json.loads(jsonResponse)
        
        status = objs['status']
        
        if status == 'OK':
            lat = objs['results'][0]['geometry']['location']['lat']
            lng = objs['results'][0]['geometry']['location']['lng']
            conn = psycopg2.connect(conn_string)
            cursor = conn.cursor()
            cursor.execute("update registry_entry set geo_lat = " + str(lat) + ", geo_long = "  + str(lng) + " where id = " + str(id) + ";")
            conn.commit()
            conn.close()
            successcount = successcount + 1
            print(str(successcount) + "/" + str(totalcount))
            
            time.sleep(.1) #avoid request rate quota
main()
