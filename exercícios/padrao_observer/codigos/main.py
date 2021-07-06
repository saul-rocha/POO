from observer import *

pub = Publisher(["Almoço", "Jantar"])
saul = Subscriber("Saul")
antonio = Subscriber("Antonio")
filip = Subscriber("Filip")

pub.registrar("Almoço", saul)
pub.registrar("Jantar", antonio)
pub.registrar("Almoço", filip)
pub.registrar("Jantar", filip)



print("Notificando...")
pub.despacho("Almoço", "Hora do Almoço!")
pub.despacho("Jantar", "O Jantar está servido!")
