import json
import requests
import urllib

import edrcmdrprofile
import RESTFirebase
import edrconfig

class EDRServer(object):

    def __init__(self):
        config = edrconfig.EDRConfig()
        self.REST_firebase = RESTFirebase.RESTFirebaseAuth()
        self.EDR_API_KEY = config.edr_api_key()
        self.EDR_ENDPOINT = config.edr_endpoint()


    def login(self, email, password):
        self.REST_firebase.api_key = self.EDR_API_KEY
        self.REST_firebase.email = email
        self.REST_firebase.password = password

        return self.REST_firebase.authenticate()

    def logout(self):
        self.REST_firebase.clear_authentication()

    def is_authenticated(self):
        return self.REST_firebase.is_valid_auth_token()

    def uid(self):
        return self.REST_firebase.uid()

    def auth_token(self):
        return self.REST_firebase.id_token()


    def server_version(self):
        endpoint = "{server}/version/.json".format(server=self.EDR_ENDPOINT)
        resp = requests.get(endpoint)
        
        if resp.status_code != 200:
            print "[EDR]Failed to check for version update. code={code}, content={content}".format(code=resp.status_code, content=resp.content)
            return None

        json_resp = json.loads(resp.content)
        return json_resp


    def system_id(self, star_system):
        query_params = "orderBy=\"name\"&equalTo={system}&limitToFirst=1&auth={auth}".format(system=json.dumps(star_system), auth=self.auth_token())
        resp = requests.get("{server}/v1/systems.json?{query_params}".format(
        server=self.EDR_ENDPOINT, query_params=query_params))

        if resp.status_code != 200:
            print "[EDR]Failed to retrieve star system sid."
            return None

        if resp.content == 'null':
            query_params = { "auth" : self.auth_token() }
            resp = requests.post("{server}/v1/systems.json?{query_params}".format(server=self.EDR_ENDPOINT, query_params=urllib.urlencode(query_params)), json={"cname": star_system.lower(), "name": star_system, "uid" : self.uid()})
            if resp.status_code != 200:
                print "[EDR]Failed to create new star system."
                return None
            sid = json.loads(resp.content).values()[0]
        else:
            sid = json.loads(resp.content).keys()[0]

        return sid


    def cmdr(self, cmdr, autocreate=True):
        cmdr_profile = edrcmdrprofile.EDRCmdrProfile()
        query_params = "orderBy=\"name\"&equalTo={cmdr}&limitToFirst=1&auth={auth}".format(cmdr=json.dumps(cmdr), auth=self.auth_token())
        endpoint = "{server}/v1/cmdrs.json?{query_params}".format(
            server=self.EDR_ENDPOINT, query_params=query_params)
        print "[EDR]Endpoint :" + endpoint
        resp = requests.get(endpoint)

        if resp.status_code != 200:
            print "[EDR]Failed to retrieve cmdr id."
            print "[EDR]{error}, {content}".format(error=resp.status_code, content=resp.content)
            return None

        if resp.content == 'null':
            if autocreate:
                query_params = { "auth" : self.auth_token() }
                endpoint = "{server}/v1/cmdrs.json?{query_params}".format(server=self.EDR_ENDPOINT, query_params=urllib.urlencode(query_params))
                resp = requests.post(endpoint, json={"name": cmdr, "cname": cmdr.lower(), "uid" : self.uid()})
                if resp.status_code != 200:
                    print "[EDR]Failed to retrieve cmdr key."
                    return None
                json_cmdr = json.loads(resp.content)
                print "[EDR] new cmdr:{}".format(json_cmdr )
                cmdr_profile.cid = json_cmdr.values()[0]
                cmdr_profile.name = cmdr
            else:
                return None
        else:
            json_cmdr = json.loads(resp.content)
            print "[EDR] existing cmdr:{}".format(json_cmdr )
            cmdr_profile.cid = json_cmdr.keys()[0]
            cmdr_profile.from_dict(json_cmdr.values()[0])

        return cmdr_profile


    def blip(self, cmdr_id, info):
        info["uid"] = self.uid()
        print "[EDR]Blip for cmdr {cid} with json:{json}".format(cid=cmdr_id, json=info)
        query_params = { "auth" : self.auth_token()}
        endpoint = "{server}/v1/blips/{cmdr_id}/.json?{query_params}".format(server=self.EDR_ENDPOINT, cmdr_id=cmdr_id, query_params=urllib.urlencode(query_params))
        print "[EDR]Endpoint :" + endpoint
        resp = requests.post(endpoint, json=info)

        return resp.status_code == 200


    def traffic(self, system_id, info):
        info["uid"] = self.uid()
        print "[EDR]Traffic report for system {sid} with json:{json}".format(sid=system_id, json=info)
        query_params = { "auth" : self.auth_token()}
        endpoint = "{server}/v1/traffic/{system_id}/.json?{query_params}".format(server=self.EDR_ENDPOINT, system_id=system_id, query_params=urllib.urlencode(query_params))
        print "[EDR]Endpoint :" + endpoint
        resp = requests.post(endpoint, json=info)

        return resp.status_code == 200


    def crime(self,  system_id, info):
        info["uid"] = self.uid()
        print "[EDR]Crime report for system {sid} with json:{json}".format(sid=system_id, json=info)
        query_params = { "auth" : self.auth_token()}
        endpoint = "{server}/v1/crimes/{system_id}/.json?{query_params}".format(server=self.EDR_ENDPOINT, system_id=system_id, query_params=urllib.urlencode(query_params))
        resp = requests.post(endpoint, json=info)

        return resp.status_code == 200