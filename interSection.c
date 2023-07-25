#include <stdio.h>

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
typedef struct ListNode ListNode;

struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB)
{
    ListNode *cursorA = headA;
    ListNode *cursorB = headB;
    ListNode *tailA = NULL;
    ListNode *tailB = NULL;
    int lA_len = 0;
    int lB_len = 0;
    int diff = 0;

    if (headA == NULL || headB == NULL)
    {
        return NULL;
    }

    while (cursorA != NULL || cursorB != NULL)
    {
        if (cursorA != NULL)
        {
            lA_len++;
            if (cursorA->next == NULL)
                tailA = cursorA;
            cursorA = cursorA->next;
        }
        if (cursorB != NULL)
        {
            lB_len++;
            if (cursorB->next == NULL)
                tailB = cursorB;
            cursorB = cursorB->next;
        }
    }
    // printf("Here\n");
    // printf("%p, %p\n", tailA, tailB);

    if (tailA != tailB)
    {
        return NULL;
    }

    cursorA = headA;
    cursorB = headB;

    if (lA_len > lB_len)
    {
        diff = lA_len - lB_len;
        while (diff > 0)
        {
            cursorA = cursorA->next;
            diff--;
        }
    }

    if (lB_len > lA_len)
    {
        diff = lB_len - lA_len;
        while (diff > 0)
        {
            cursorB = cursorB->next;
            diff--;
        }
    }

    while (cursorA != NULL && cursorB != NULL)
    {
        if (cursorA == cursorB)
            return cursorA;
        cursorA = cursorA->next;
        cursorB = cursorB->next;
    }

    return NULL;
}
