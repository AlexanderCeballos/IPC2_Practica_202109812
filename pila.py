from nodo import Nodo
import graphviz
import base64

class Pila:
    def __init__(self):
        self.tope = None
        self.valor = None

    def insertar(self, valor):
        if self.tope == None:
            self.tope = Nodo(valor)
        else:
            nodoTemp = Nodo(valor)
            nodoTemp.setSiguiente(self.tope)
            self.tope = nodoTemp

    def printPila(self):
        nodoTemp = self.tope
        listaDatos = ""

        while nodoTemp != None:
            listaDatos += nodoTemp.getValor()
            nodoTemp = nodoTemp.getSiguiente()

        return listaDatos
    
    def generarDot(self):
        nodoTemp = self.tope
        dot = graphviz.Digraph('structs', filename='structs.gv', node_attr={'shape': 'none', 'fontname':'Helvetica'})
        
        strTabla = "<table>"

        while(nodoTemp != None):
            strTabla += f'<tr><td width="60" height="60" border="5" bgcolor = "#509c61">{nodoTemp.getValor()}</td></tr>'
            nodoTemp = nodoTemp.getSiguiente()
        
        strTabla += "</table>"

        dot.node('n', label='<' +strTabla+'>')
        dot.render(outfile='graficas/structs.png').replace('\\', '/')
        'img/structs.png'

        return "La imagen ha sido generada"
    
    def obtenerBase64(self):
        with open('graficas/structs.png', 'rb') as f:
            image = f.read()

        encoded_bytes = base64.b64encode(image)
        encoded_string = encoded_bytes.decode('utf-8')

        print(encoded_string)

        return encoded_string
