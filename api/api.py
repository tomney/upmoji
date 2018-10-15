import json

BASE_CLASS_PROPERTIES = ["request", "arguments"]

class ApiMissingArgumentError(Exception):
    pass

class ApiHandler:
    request = None
    arguments = {}

    def _init_(self, request = None):
        self.request = request
        if request:
            self.arguments = json.loads(request)
        try:
            self._validate()
        except ApiMissingArgumentError:
            # TODO figure out how to return 400 from flask
            pass
        return self._process()
            
    def _validate(self):
        for key in self.__dict__.keys():
            if not key.startswith("_") and not key in BASE_CLASS_PROPERTIES and not self.arguments.get(key):
                raise ApiMissingArgumentError("Did not specify '{}'.".format(key))

    def _process(self):
        pass
        
