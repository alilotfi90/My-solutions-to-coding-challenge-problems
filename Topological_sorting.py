import graph_implementation_dictionary as g
def helper_func(graph1,current,visited,result):
  visited[current]=True
  for neighbor in graph1.graph[current]:
    if visited[neighbor]==False:
      helper_func(graph1,neighbor,visited,result)
  result.insert(0,current)
def topsorting(graph1):
  result=[]
  visited={}

  for i in graph1.vertices:
    visited[i]=False
  for current in graph1.vertices:
    if visited[current]==False:
      helper_func(graph1,current,visited,result)
  return result


def main():
    grph=g.Graph([1,2,3,4,5])
    for i in range(1,5):
      for j in range(i+1,5):
        grph.addEdge(i,j)
    print(topsorting(grph))
    ls=[0,1,2,3,4]
    i=2
    print(ls[0:2])
    for i in range(1,2):
      print(i)
if __name__ == "__main__":
  main()


  ##############
