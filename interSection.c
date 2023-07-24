/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB)
{
	ListNode *cursorA = headA;
	ListNode *cursorB = headB;
	int l1_len = 0;
	int l2_len = 0;
	

	while (cursorA != NULL || cursorB != NULL)
	{
		if (cursorA != NULL)
		{
			l1_len++;
			cursorA = cursorA->next
		}
		if (cursorB != NULL)
		{
			l2_len++;
			cursorB = cursorB->next
		}
	}
}
