from passlib.context import CryptContext

pln_text = CryptContext(schemes=["bcrypt"], deprecated = "auto")
# helper for hashing passwwords using bcrypt

class Hash():
    def encrypt(password:str):
        return pln_text.hash(password)
    #this function encrypts the password provided provided by the user and stores it in the database alongside the username
    
    def verify(password_hash, password):
        return pln_text.verify(password, password_hash)
    #this function checks/verifies whether the entered password has the same hash value as the on epresent in the databse.



