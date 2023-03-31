class MedianFinder {
    PriorityQueue<Integer> smallPQ;
    PriorityQueue<Integer> bigPQ;

    public MedianFinder() {
        smallPQ = new PriorityQueue<>(Collections.reverseOrder());
        bigPQ = new PriorityQueue<>();
    }
    
    public void addNum(int num) {

        if(bigPQ.size() > 0 && num > bigPQ.peek()){
            bigPQ.add(num);
        }
        else{
            smallPQ.add(num);
        }
        if(smallPQ.size() > bigPQ.size() + 1){
            bigPQ.add(smallPQ.poll());
        }
        else if(bigPQ.size() > smallPQ.size()+1){
            smallPQ.add(bigPQ.poll());
        }
        // System.out.println("smallPQ:" + smallPQ);
        // System.out.println("bigPQ:" + bigPQ);
        
    }
    
    public double findMedian() {
        if(smallPQ.size() >bigPQ.size()){
            return smallPQ.peek()*1.0;
        }

        if(bigPQ.size() >smallPQ.size()){
            return bigPQ.peek()*1.0;
        }
        
        return (smallPQ.peek()+bigPQ.peek())/2.0;
        

        
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */