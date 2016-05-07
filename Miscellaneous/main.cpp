#include <cstdio>
#include <iostream>
#include <list>
#include <queue>
#define MAX 10
#define IDLE 0
#define UP 1
#define DOWN 2

using namespace std;

bool up_to[MAX], up_from[MAX];
bool down_from[MAX], down_to[MAX];

//up_to[i] means there has a user on the ith floor want to go up
//up_from[i] means there has a user in the elevator need to disembark on the ith floor

struct Elevator
{
    int max_to = 0, max_from = 0, current_floor = 1;
    
    void run() {
        while (go_up())
            ;
        while (go_down())
            ;
    }
    
    bool go_up() {
        cout << "Elevator is on the floor " << current_floor << endl;
        //Go to max from;
        if (up_from[current_floor])
            cout << "There are some users on floor " << current_floor << " wanna go up, elevator stops." << endl;
        
        if (up_to[current_floor])
            cout << "There are some users in the elevator " << " wanna go to floor " << current_floor << " elevator stops." << endl;
        
        int max_floor = max(max_from, max_to);
        
        if (current_floor >= max_floor) {
            return false;
            //Start to go down.
        } else {
            current_floor++; // Go up.
            return true;
        }
    }
    
    bool go_down() {
        //Go to first floor;
        if (down_from[current_floor])
            cout << "There are some users on floor " << current_floor << " wanna go down, elevator stops." << endl;
        
        cout << "Elevator is on the floor " << current_floor << endl;
        
        if (down_to[current_floor])
            cout << "There are some users in the elevator " << "wanna go to floor " << current_floor << " elevator stops." << endl;
        
        
        if (current_floor == 1) {
            return false;
            //Elevator has already back to first floor.
        } else {
            current_floor--; // Go down.
            return true;
        }
    }
    
    void call(int _from, int _direction, int _to) {
        if (_direction == UP) {
            up_to[_to] = true;
            up_from[_from] = true;
        } else {
            down_to[_to] = true;
            down_from[_from] = true;
        }
        
        max_from = max(max_from, _from);
        max_to = max(max_to, _to);
    }
    
    void init() {
        int n, _from, _to;
        
        printf("Please input the number of people.\n");
        
        cin >> n;
        getchar();
        while(n--) {
            scanf("from %d to %d", &_from, &_to);
            getchar();
            int direction = _from > _to ? DOWN : UP;
            
            call(_from, direction, _to);
        }
    }
};

int main()
{
    Elevator e;
    
    e.init();
    e.run();
    
    return 0;
}

