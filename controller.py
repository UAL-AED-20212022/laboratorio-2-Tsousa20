from models.LinkedList import LinkedList

def inserir_pais_inicio(lista_paises, pais_novo):
    lista_paises.insert_at_start(pais_novo)
    return lista_paises

def inserir_pais_fim(lista_paises, pais_novo):
    lista_paises.insert_at_end(pais_novo)
    return lista_paises

def inserir_pais_depois_elemento(lista_paises, pais_novo, pais_registado):
    lista_paises.insert_after_item(pais_registado, pais_novo)
    return lista_paises

def inserir_pais_antes_elemento(lista_paises, pais_novo, pais_registado):
    lista_paises.insert_before_item(pais_registado, pais_novo)
    return lista_paises

def inserir_pais_indice(lista_paises, pais_novo, indice):
    lista_paises.insert_at_index(indice, pais_novo)
    return lista_paises

def verificar_numero_elementos(lista_paises):
    count = lista_paises.get_count()
    return count

def verificar_pais(lista_paises, pais):
    if lista_paises.search_item(pais) == True:
        return True
    else:
        return False

def eliminar_primeiro_elemento(lista_paises):
    primeiro_elemento = lista_paises.start_node.item
    lista_paises.delete_at_start()
    return primeiro_elemento

def eliminar_ultimo_elemento(lista_paises):
    ultimo_elemento = lista_paises.get_last_node()
    lista_paises.delete_at_end()
    return ultimo_elemento

# verifico, primeiro, se o país pertence à lista, e depois elimino
def eliminar_determinado_elemento(lista_paises, pais):
    if lista_paises.search_item(pais) == True:
        lista_paises.delete_element_by_value(pais)
        return True
    else:
        return False
    
     
    