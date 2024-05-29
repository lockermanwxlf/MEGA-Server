from mega import MegaApi
from executor import Executor 
   

class Mega:
    def __init__(self) -> None:
        self.logged_in = False
        self.executor = Executor(logging=True)
        self.api = MegaApi("megaserver", "/app/cache")
        self.api.addListener(self.executor.listener)
        
    def login(self, email: str, password: str):
        print("Logging in ", email, password, flush=True)
        self.executor.execute(self.api.login, email, password)
        self.executor.execute(self.api.fetchNodes)
        self.executor.execute(self.api.getAccountDetails)
        
    def does_file_exist(self, path: str):
        path = "/" + path.lstrip("/")
        node = self.api.getNodeByPath(path)
        print(node, flush=True)
        return node is not None
    
    def upload_file(self, mega_path: str, local_path: str):
        mega_path = "/" + mega_path.lstrip("/")
        split = mega_path[1:].split("/")
        dir_path = "/" + "/".join(split[0:-1])
        node = self.api.getNodeByPath(dir_path)
        if node is None:
            print("Making folders.", flush=True)
            node = self.api.getNodeByPath("/")
            for segment in split[0:-1]:
                if not self.api.getNodeByPath(segment, node):
                    self.executor.execute(self.api.createFolder, segment, node)
                node = self.api.getNodeByPath(segment, node)
        self.api.startUpload(
            local_path,
            node,
            0, # modification time
            True # delete local file after upload
        )