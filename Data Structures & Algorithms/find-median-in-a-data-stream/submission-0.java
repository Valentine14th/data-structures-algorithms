class MedianFinder {
    private Queue<Integer> large;
    private Queue<Integer> small;


    public MedianFinder() {
        large = new PriorityQueue<Integer>();
        small = new PriorityQueue<Integer>(Collections.reverseOrder());
    }
    
    public void addNum(int num) {
        if(this.small.isEmpty() || num <= this.small.peek()){
            this.small.add(num);
        }
        else{
            this.large.add(num);
        }
        if(this.small.size() > this.large.size() + 1){
            int temp = this.small.poll();
            this.large.add(temp);
        }
        if(this.large.size() > this.small.size() + 1){
            int temp = this.large.poll();
            this.small.add(temp);
        }
        
    }
    
    public double findMedian() {
        if(this.small.size() > this.large.size()){
            return this.small.peek();
        }
        if(this.large.size() > this.small.size()){
            return this.large.peek();
        }
        else{
            return (this.small.peek() + this.large.peek()) / 2.0;
        }

        
    }
}
