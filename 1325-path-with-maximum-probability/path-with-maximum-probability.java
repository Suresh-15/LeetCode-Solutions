class Solution {
    static class Pair {
        int node;
        double prob;
        Pair(int node, double prob) {
            this.node = node;
            this.prob = prob;
        }
    }

    public double maxProbability(
        int n, int[][] edges, double[] succProb, int start, int end
    ) {
        List<List<Pair>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) 
            graph.add(new ArrayList<>());

        for (int i = 0; i < edges.length; i++) {
            int a = edges[i][0], b = edges[i][1];
            double prob = succProb[i];
            graph.get(a).add(new Pair(b, prob));
            graph.get(b).add(new Pair(a, prob));
        }

        PriorityQueue<Pair> maxHeap = new PriorityQueue<>((a, b) -> Double.compare(b.prob, a.prob));
        maxHeap.add(new Pair(start, 1.0));

        double[] maxProb = new double[n];
        maxProb[start] = 1.0;

        while (!maxHeap.isEmpty()) {
            Pair current = maxHeap.poll();
            int node = current.node;
            double currProb = current.prob;

            if (node == end) 
                return currProb;

            for (Pair neighbor : graph.get(node)) {
                int nextNode = neighbor.node;
                double edgeProb = neighbor.prob;
                double newProb = currProb * edgeProb;

                if (newProb > maxProb[nextNode]) {
                    maxProb[nextNode] = newProb;
                    maxHeap.add(new Pair(nextNode, newProb));
                }
            }
        }
        return 0.0;
    }
}