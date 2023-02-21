from passlib.context import CryptContext

pln_text = CryptContext(schemes=["bcrypt"], deprecated = "auto")
# helper for hashing passwwords using bcrypt

class Hash():
    def encrypt(password:str):
        return pln_text.hash(password)
    
    def verify(password_hash, password):
        return pln_text.verify(password, password_hash)



