import mongoengine

class Palavra(mongoengine.EmbeddedDocument):

    _id = mongoengine.SequenceField(required=True, primary_key=True)
    termo = mongoengine.StringField(null=True, default= "TERMO TESTE")
    traducao = mongoengine.StringField(null=True, default= "TRADUÇÃO TESTE")

    def setTermo(self, termo):
        self.termo = termo

    def getTermo(self):
        return self.termo

    def setTraducao(self, traducao):
        self.traducao = traducao

    def getTraducao(self):
        return self.traducao