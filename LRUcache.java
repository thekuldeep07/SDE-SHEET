import java.util.HashMap;

import org.graalvm.compiler.graph.Node;

public class LRUcache {
    Node head = new Node(0,0);
    Node tail = new Node(0.0);
    HashMap<Integer,Node> hmp = new HashMap<>();
    int capacity;


    public LRUcache(int capacity){
        this.capacity=capacity;
        head.next=tail;
        tail.prev=head;
    }
    
    public void put(int Key , int value){
        if (hmp.containsKey(key)){
            remove(map.get(key));            
        }
        if(hmp.size() ==capacity){
            remove(tail.prev);
        }
        insert(new Node(key,value));
    }

    public int get(int key) {
        if(map.containsKey(key)) {
          Node node = map.get(key);
          remove(node);
          insert(node);
          return node.value;
        } else {
          return -1;
        }
      }

    private void insert(Node node){
        map.put(node.key, node);
        node.next = head.next;
        node.next.prev = node;
        head.next = node;
        node.prev = head;
      }

    private void remove(Node node){
         hmp.remove(node.key);
         node.prev.next = node.next;
         node.next.prev = node.prev;

    }
    
}
public class Node{
    Node next , prev;
    int key , value;

    public Node(int key , int value){
        this.key=key;
        this.value=value;
    }
}


