import logging


# FOR CLIENT
class ClientConfig:
    SERVER_URI = "ws://localhost:8080"
    CONSOLE_LOG_LEVEL = logging.WARNING
    FILE_LOG_LEVEL = logging.INFO


# FOR SERVER
class ServerConfig:
    HOST = ""
    PORT = 8080
