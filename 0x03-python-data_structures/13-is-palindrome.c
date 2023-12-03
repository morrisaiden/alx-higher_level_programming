#include "lists.h"

listint_t *reverse_list(listint_t **head)
{
    listint_t *prev = NULL, *current = *head, *next;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;
    return *head;
}

int is_palindrome(listint_t **head)
{
    if (*head == NULL || (*head)->next == NULL)
        return 1;

    listint_t *slow = *head, *fast = *head, *prev_slow = *head;
    listint_t *second_half, *reversed_second_half;

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev_slow = slow;
        slow = slow->next;
    }

    if (fast != NULL)
        slow = slow->next;

    second_half = slow;
    reversed_second_half = reverse_list(&second_half);

    while (reversed_second_half != NULL)
    {
        if ((*head)->n != reversed_second_half->n)
            return 0;

        *head = (*head)->next;
        reversed_second_half = reversed_second_half->next;
    }

    reverse_list(&second_half);
    prev_slow->next = second_half;

    return 1;
}

