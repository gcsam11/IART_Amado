import random
from collections import deque

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4
START = 0

# A generic definition of a state of the problem

red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

color_string = ["yellow", "blue", "red"]
move_string = ["START", "UP", "DOWN", "LEFT", "RIGHT"]
colors = [(255, 255, 0), (0, 0, 255), (255, 0, 0)]
colors_dic={(255, 255, 0):0, (0, 0, 255):1, (255, 0, 0):2}

game_board_start = [[red,yellow,blue,red],[blue,blue,yellow,red],[yellow,yellow,blue,yellow],[blue,yellow,yellow,red]]  # Different color for each square
game_board_solution = [[blue,red,red,yellow],[yellow,red,blue,red],[yellow,red,red,yellow],[red,yellow,red,red]]

def copy(board):
    new_board = []
    for i in range(len(board)):
        temp = board[i].copy()
        new_board.append(temp)
    return new_board

def list_to_tuple(l):
    return tuple([tuple(x) for x in l])


class GameState:
    def __init__(self,cursor_position,board,goal_board,previous_move=START):
        self.cursor_position = cursor_position
        self.board = board
        self.goal_board = goal_board
        self.previous_move = previous_move
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.cursor_position == self.cursor_position and other.board == self.board
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __hash__(self):
        return hash((self.cursor_position, list_to_tuple(self.board)))

    def __str__(self):
        string = "(" + str(self.cursor_position[0]) + ", " + str(self.cursor_position[1]) + ")\n\n"

        for i in range(len(self.board)):
            string += "["
            for j in range(len(self.board[i])):
                string += color_string[colors_dic[self.board[i][j]]]
                if j != len(self.board[i]) - 1:
                    string += ","
            string += "]\n"

        return string
    
    ###SMOOTH OPERATORS

    def color_update(pos,next_pos,board):
        b = copy(board)
        first_color = board[pos[1]][pos[0]]
        second_color = board[next_pos[1]][next_pos[0]]
        if(first_color == second_color):
            return board
        else:
            remaining_color = 3 - colors_dic[first_color] - colors_dic[second_color]
            b[next_pos[1]][next_pos[0]] = colors[remaining_color]
            return b

    def up(state):
        if(state.cursor_position[1] <= 0):
            return state
        else:
            new_cursor = (state.cursor_position[0],state.cursor_position[1]-1)
            new_board = GameState.color_update(state.cursor_position,new_cursor,state.board)
            return GameState(new_cursor,new_board,state.goal_board,UP)
        
    def down(state):
        if(state.cursor_position[1] >= len(state.board) - 1):
            return state
        else:
            new_cursor = (state.cursor_position[0],state.cursor_position[1]+1)
            new_board = GameState.color_update(state.cursor_position,new_cursor,state.board)
            return GameState(new_cursor,new_board,state.goal_board,DOWN)
    
    def left(state):
        if(state.cursor_position[0] <= 0):
            return state
        else:
            new_cursor = (state.cursor_position[0]-1,state.cursor_position[1])
            new_board = GameState.color_update(state.cursor_position,new_cursor,state.board)
            return GameState(new_cursor,new_board,state.goal_board,LEFT)
    
    def right(state):
        if(state.cursor_position[0] >= len(state.board[0]) - 1):
            return state
        else:
            new_cursor = (state.cursor_position[0]+1,state.cursor_position[1])
            new_board = GameState.color_update(state.cursor_position,new_cursor,state.board)
            return GameState(new_cursor,new_board,state.goal_board,RIGHT)
        
    def get_states(state):
        new_states = []
        
        up_state = GameState.up(state)
        if(up_state != state):
            new_states.append(up_state)
        
        down_state = GameState.down(state)
        if(down_state != state):
            new_states.append(down_state)
        
        left_state = GameState.left(state)
        if(left_state != state):
            new_states.append(left_state)

        right_state = GameState.right(state)
        if(right_state != state):
            new_states.append(right_state)
        
        return new_states
    
    def goal_state(state):
        res = state.board == state.goal_board
        g = True
        for i in range(len(state.board)):
            for j in range(len(state.board[i])):
                if(state.board[i][j] != state.goal_board[i][j]):
                    g = False
            
        return g
    
    def heuristic(state):
        board = state.board
        goal_board = state.goal_board
        distance = 0

        for i in range(len(board)):
            for j in range(len(board[i])):
                if(board[i][j] != goal_board[i][j]):
                    distance += 1
        return distance
        
        
# A generic definition of a tree node holding a state of the problem
class TreeNode:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        if self.parent is None:
            self.depth = 0
        else:
            self.depth = self.parent.depth +1

    def add_child(self, child_node):
        self.children.append(child_node)
        child_node.parent = self
        child_node.depth = self.depth + 1

    def breadth_first_search(initial_state, goal_state_func, operators_func):
        root = TreeNode(initial_state)   # create the root node in the search tree
        queue = deque([root])   # initialize the queue to store the nodes
        
        while queue:
            node = queue.popleft()
            if goal_state_func(node.state):
                return node
            else:
                new_states = operators_func(node.state)
                for state in new_states:
                    new_node = TreeNode(state)
                    node.add_child(new_node)
                    queue.append(new_node)
            
            

        return None
    
    def depth_first_search(initial_state, goal_state_func, operators_func):
        root = TreeNode(initial_state)
        stack = [root]

        while stack:
            node = stack.pop()
            if goal_state_func(node.state):
                return node
            else:
                new_states = operators_func(node.state)
                for state in new_states:
                    new_node = TreeNode(state)
                    node.add_child(new_node)
                    stack.append(new_node)
            
            print("Stack length: ", len(stack))
    
        return None
    
    def greedy_search(initial_state, goal_state_func, operators_func, heuristic_func):
        root = TreeNode(initial_state)
        open_list = [root]
        closed_list = []

        while open_list:
            open_list.sort(key=lambda x: heuristic_func(x.state))
            node = open_list.pop(0)
            closed_list.append(node)
            if goal_state_func(node.state):
                return node
            else:
                new_states = operators_func(node.state)
                for state in new_states:
                    new_node = TreeNode(state)
                    node.add_child(new_node)
                    if new_node not in closed_list:
                        open_list.append(new_node)
            
            print("Open list length: ", len(open_list))
            print("Closed list length: ", len(closed_list))
    
        return None
    
    def a_star_search(initial_state, goal_state_func, operators_func, heuristic_func):
        root = TreeNode(initial_state)
        open_list = [root]
        closed_list = []

        while open_list:
            open_list.sort(key=lambda x: heuristic_func(x.state) + x.depth)
            node = open_list.pop(0)
            closed_list.append(node)
            if goal_state_func(node.state):
                return node
            else:
                new_states = operators_func(node.state)
                new_states.sort(key=lambda x: heuristic_func(x))
                for state in new_states:
                    new_node = TreeNode(state)
                    node.add_child(new_node)
                    if new_node not in closed_list:
                        open_list.append(new_node)
            
            print("Open list length: ", len(open_list))
            print("Closed list length: ", len(closed_list))
    
        return None
    
    def depth_limited_search(initial_state, goal_state_func, operators_func, depth_limit):
        # your code here
        root = TreeNode(initial_state)
        visited = set ([initial_state])

        '''inner recursive function'''

        def sub_dfs(node,depth):
            if goal_state_func(node.state):
                return node
            if depth == depth_limit:
                return None
            
            for state in operators_func(node.state):
                if(state not in visited):
                    visited.add(state)
                    child_node = TreeNode(state=state,parent=node)
                    node.add_child(child_node)
                    goal = sub_dfs(child_node,depth+1)
                    if(goal is not None):
                        return goal
            
            return None
    
        return sub_dfs(root,0)

    def iterative_deepening_search(initial_state, goal_state_func, operators_func, max_depth):
        # your code here
        for depth in range(max_depth):
            print(depth)
            result = TreeNode.depth_limited_search(initial_state,goal_state_func,operators_func,depth)
            if result is not None:
                return result
        
        return None

    
    def print_solution(node):
        # your code here
        if node:
            path = []
            while node:
                path.append(node)
                node = node.parent
            print(f"Found goal state in {len(path)-1} steps:")
            path = reversed(path)
            for step in path:
                print(move_string[step.state.previous_move])
        
        
        return
    
goal = TreeNode.depth_limited_search(GameState((0,0),game_board_start,game_board_solution),GameState.goal_state,GameState.get_states,50)

TreeNode.print_solution(goal)

print(goal.state)

print("Done")