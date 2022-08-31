#def tri_iteratif(tab):
#
#    for k in range( ... , 0, -1):
#
#        for i in range(0 , ... ):
#
#            if tab[i] > ... :
#                ... , tab[i] = tab[i] , ...
#    return tab


l = [41,55,21,18,12,6,25]

def tri_iteratif(tab):

    for k in range(len(tab), 0, -1):

        for i in range(0 ,len(tab)-k):

            if tab[i] > tab[-k]:

                tab[-k] , tab[i] = tab[i] , tab[-k]

    return tab
