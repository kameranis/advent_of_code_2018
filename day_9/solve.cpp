#include<cstdio>
#include<algorithm>
#include<memory>
#include<utility>

class Node: public std::enable_shared_from_this<Node> {
    public:
    unsigned long long data;
    std::shared_ptr<Node> prev, next;

    Node() {this->data = 0; this->prev = this->next = nullptr;}
    Node(unsigned long long d) {this->data = d; this->prev = this->next = nullptr;}

    void add_after(std::shared_ptr<Node> next_Node) {
        next_Node->next = this->next;
        next_Node->prev = shared_from_this();
        this->next->prev = next_Node;
        this->next = next_Node;
    }

    void add_before(std::shared_ptr<Node> prev_Node) {
        return this->prev->add_after(prev_Node);
    }

    unsigned long long delete_next() {
        auto deleted_node = this->next;
        this->next = this->next->next;
        this->next->prev = shared_from_this();

        deleted_node->prev = nullptr;
        deleted_node->next = nullptr;
        return deleted_node->data;
    }

    unsigned long long delete_before() {
        return this->prev->prev->delete_next();
    }

    void print_list() {
        printf("%llu", this->data);
        for(auto it = this->next; it != shared_from_this(); it = it->next) {
            printf(" %llu", it->data);
        }
        printf("\n");
    }
};


int main() {
    int players, marbles;
    scanf("%d players; last marble is worth %d", &players, &marbles);

    unsigned long long score[players] = { 0 };
    printf("Initialized list\n");
    std::shared_ptr<Node> current_Node(new Node(0));
    current_Node->next = current_Node->prev = current_Node;
    int current_player = 0;
    for(int i=1; i <= marbles; i++) {
        // current_Node->print_list();
        if(i % 23 == 0) {
            current_Node = current_Node->prev->prev->prev->prev->prev->prev;
            score[current_player] += i + current_Node->delete_before();
        }
        else {
            std::shared_ptr<Node> new_Node(new Node(i));
            current_Node = current_Node->next;
            current_Node->add_after(new_Node);
            current_Node = current_Node->next;
        }
        current_player = (current_player + 1) % players;
    }

    printf("High score is %llu\n", *std::max_element(score, score + players));
}

