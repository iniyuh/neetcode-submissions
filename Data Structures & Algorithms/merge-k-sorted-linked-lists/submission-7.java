/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> minHeap = new PriorityQueue<>((a, b) -> Integer.compare(a.val, b.val));

        ListNode head = new ListNode();
        ListNode curr = head;
        for (ListNode node : lists) minHeap.offer(node);

        while (minHeap.size() > 0) {
            ListNode node = minHeap.poll();
            if (node.next != null) minHeap.offer(node.next);

            curr.next = node;
            curr = node;
        }

        return head.next;
    }
}
