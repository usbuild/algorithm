#include <iostream>
using namespace std;
struct ListNode{
    int m_nKey;
    ListNode* m_pNext;
};

ListNode* searchKth(ListNode* start, int k){
    ListNode* first = start;
    ListNode* last = start;
    for (int i = 0; i < k; i++) {
        if (last == NULL) return NULL;
        last = last->m_pNext;
    }
    while(last->m_pNext != NULL) {
        last = last->m_pNext;
        first = first->m_pNext;
    }
    return first;
}

int main(int argc, const char *argv[])
{
    return 0;
}
