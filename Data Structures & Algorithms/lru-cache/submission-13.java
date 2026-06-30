public class Node {
    int key;
    int val;
    Node prev;
    Node next;

    public Node(int key, int val) {
        this.key = key;
        this.val = val;
        this.prev = null;
        this.next = null;
    }
}

class LRUCache {

    private int capacity;
    private Node head;
    private Node tail;
    private HashMap<Integer, Node> hm;

    private void promote(Node target) {
        if (target.next.equals(tail)) return;

        Node p = target.prev, n = target.next;

        Node p_ = tail.prev;
        p_.next = target;
        target.prev = p_;

        target.next = tail;
        tail.prev = target;

        p.next = n;
        n.prev = p;
    }

    private void evict() {
        Node target = head.next;
    }

    private void print() {
        Node curr = head;
        while (curr != null) {
            System.out.print("[" + curr.key + ", " + curr.val + "]");
            curr = curr.next;
        }
        System.out.println();
        System.out.print(hm.size());
        System.out.println();
    }

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.head = new Node(0, 0);
        this.tail = new Node(0, 0);

        this.head.next = this.tail;
        this.tail.prev = this.head;

        this.hm = new HashMap<>();
    }
    
    public int get(int key) {
        if (hm.containsKey(key)) {
            Node target = hm.get(key);
            promote(target);
            print();
            return target.val;
        }
        else {
            print();
            return -1;
        }
    }
    
    public void put(int key, int value) {
        if (hm.containsKey(key)) {
            Node target = hm.get(key);
            target.val = value;
            promote(target);
        }
        else  {
            Node newNode = new Node(key, value);

            Node p = tail.prev;
            p.next = newNode;
            newNode.prev = p;

            newNode.next = tail;
            tail.prev = newNode;

            hm.put(key, newNode);

            if (hm.size() > capacity) {
                Node target = head.next;
                Node n = target.next;

                head.next = n;
                n.prev = head;

                hm.remove(target.key);
            }
        }

        print();
    }
}
