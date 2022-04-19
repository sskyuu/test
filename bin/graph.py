class graph:
    def __init__(self):
        self.n = 0
        self.m = 0
        self.edge = []
        self.isdirected = False
    
    def setn(self,n):
        """
        頂点の数を設定。
        """
        self.n = n
        self.edge = [[] for _ in range(n)]
        #self.e = [[0 for _ in range(n)] for _ in range(n)]
    
    def setm(self,m):
        """
        辺の数を設定。
        """

        self.m = m

    def directed(self):
        """
        有効グラフにする。
        """
        self.isdirected = True

    def addEdge(self,V,indexed):
        """
        辺を追加。
        配列で渡す。
        """

        if self.isdirected:
            for i in range(len(V)):
                self.edge[V[i][0]-indexed].append(V[i][1]-indexed)
        else:
            for i in range(len(V)):
                self.edge[V[i][0]-indexed].append(V[i][1]-indexed)
                self.edge[V[i][1]-indexed].append(V[i][0]-indexed)

    def addEdgeWeight(self,V,indexed):
        """
        辺を追加。
        重み付き。
        """

        if self.isdirected:
            for i in range(len(V)):
                self.edge[V[i][0]-indexed].append((V[i][1]-indexed,V[i][2]))
        else:
            for i in range(len(V)):
                self.edge[V[i][0]-indexed].append((V[i][1]-indexed,V[i][2]))
                self.edge[V[i][1]-indexed].append((V[i][0]-indexed,V[i][2]))

    def addEdgeWeight2(self,V,indexed):
        """
        辺の更新を見越した追加。
        辺の重み0以上。
        常に安い方に更新。
        """

        if self.isdirected:
            for i in range(len(V)):
                if self.e[V[i][0]-indexed][V[i][1]-indexed] == 0:
                    self.edge[V[i][0]-indexed].append([V[i][1]-indexed,V[i][2]])
                    self.e[V[i][0]-indexed][V[i][1]-indexed] = V[i][2]
                elif self.e[V[i][0]-indexed][V[i][1]-indexed] > V[i][2]:
                    for j in range(len(self.edge[V[i][0]-indexed])):
                        if self.edge[V[i][0]-indexed][j][0] == V[i][1]-indexed:
                            self.edge[V[i][0]-indexed][j][1] = V[i][2]
                            break
                    self.e[V[i][0]-indexed][V[i][1]-indexed] = V[i][2]
        else:
            for i in range(len(V)):
                if self.e[V[i][0]-indexed][V[i][1]-indexed] == 0:
                    self.edge[V[i][0]-indexed].append([V[i][1]-indexed,V[i][2]])
                    self.edge[V[i][1]-indexed].append([V[i][0]-indexed,V[i][2]])
                    self.e[V[i][0]-indexed][V[i][1]-indexed] = V[i][2]
                    self.e[V[i][1]-indexed][V[i][0]-indexed] = V[i][2]
                elif self.e[V[i][0]-indexed][V[i][1]-indexed] > V[i][2]:
                    for j in range(len(self.edge[V[i][0]-indexed])):
                        if self.edge[V[i][0]-indexed][j][0] == V[i][1]-indexed:
                            self.edge[V[i][0]-indexed][j][1] = V[i][2]
                            break
                    for j in range(len(self.edge[V[i][1]-indexed])):
                        if self.edge[V[i][1]-indexed][j][0] == V[i][0]-indexed:
                            self.edge[V[i][1]-indexed][j][1] = V[i][2]
                            break
                    self.e[V[i][0]-indexed][V[i][1]-indexed] = V[i][2]
                    self.e[V[i][1]-indexed][V[i][0]-indexed] = V[i][2]

    def Dijkstra(self,r):
        """
        ダイクストラ法。
        rから各頂点への最短コスト。
        O(ElogV)っぽい。
        """
        import heapq
        cost = [float('inf') for _ in range(self.n)]
        cost[r] = 0
        que = []
        heapq.heappush(que,(0,r))

        while len(que) != 0:
            c,n = heapq.heappop(que)
            if cost[n] < c:
                continue
            for i in self.edge[n]:
                if cost[i[0]] < c+i[1]:
                    continue
                heapq.heappush(que,(c+i[1],i[0]))
                cost[i[0]] = min(cost[i[0]],c+i[1])
        
        return cost

    def WarshallFloyd(self,inf):
        """
        ワ―シャルフロイド法。
        O(V^3)、負の閉路があるときは自分自身へ行くのがマイナス。
        """

        if inf == 0:
            inf = float("inf")
        dp = [[inf for _ in range(self.n)] for _ in range(self.n)]
        for i in range(self.n):
            for j in self.edge[i]:
                dp[i][j[0]] = j[1]
        for i in range(self.n):
            dp[i][i] = 0
        
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    dp[i][j] = min(dp[i][j],dp[i][k]+dp[k][j])
        return dp

