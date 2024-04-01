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

# Move the cursor to the next position
def move_cursor(game_board_start, cursor_position, next_position):
        x,y = cursor_position
        next_x, next_y = next_position
        if(next_position[0] >= 0 and next_position[0] < len(game_board_start[0]) and next_position[1] >= 0 and next_position[1] < len(game_board_start)):
            if(game_board_start[next_position[1]][next_position[0]] != (0,0,0)):
                cursor_position = next_position
            else:
                return False, cursor_position
        else: 
            return False, cursor_position
        if game_board_start[next_y][next_x] != game_board_start[y][x]:
            first_color_num = colors_dic[game_board_start[y][x]]
            second_color_num = colors_dic[game_board_start[next_y][next_x]]
            remaining_color_num = 3 - first_color_num - second_color_num
            final_color = colors[remaining_color_num]
            game_board_start[next_y][next_x]=final_color
        return True, cursor_position

# Regression algorithm that does more alterations to the board with higher level difficulty
def regression_algorithm(cursor_position,game_board_start, difficulty):
        if difficulty == 1:
            steps = 5*len(game_board_start)
        elif difficulty == 2:
            steps = 10*len(game_board_start)
        elif difficulty == 3:
            steps = 20*len(game_board_start)
        original_cursor = cursor_position
        row = random.randint(0, len(game_board_start)-1)
        valid_list = [x for x in range(len(game_board_start[row])) if game_board_start[row][x] != (0,0,0)]
        col = random.choice(valid_list)
        cursor_position = (col, row)
        for _ in range(steps):
            direction = random.choice(move_string[1:])
            if direction == "UP":
                cond, cursor_position = move_cursor(game_board_start, cursor_position, (cursor_position[0], cursor_position[1]-1))
                if (not cond):
                    steps+=1
            elif direction == "DOWN":
                cond, cursor_position = move_cursor(game_board_start, cursor_position, (cursor_position[0], cursor_position[1]+1))
                if (not cond):
                    steps+=1
            elif direction == "LEFT":
                cond, cursor_position = move_cursor(game_board_start, cursor_position, (cursor_position[0]-1, cursor_position[1]))
                if (not cond):
                    steps+=1
            elif direction == "RIGHT":
                cond, cursor_position = move_cursor(game_board_start, cursor_position, (cursor_position[0]+1, cursor_position[1]))
                if (not cond):
                    steps+=1
        cursor_position = original_cursor
        return game_board_start

# Generate a solution board with random colors based on the board number
def generate_board(board, cursor_position=(0,0)):
        if board == 1:
            # 4x4 square board
            game_board_solution = [[random.choice(colors) for _ in range(4)] for _ in range(4)]
        elif board == 2:
            # 5x5 square without (1,3), (3,1), (5,3), (3,5) squares
            game_board_solution = [[random.choice(colors) for _ in range(5)] for _ in range(5)]
            game_board_solution[0][2] = (0,0,0)
            game_board_solution[2][0] = (0,0,0)
            game_board_solution[4][2] = (0,0,0)
            game_board_solution[2][4] = (0,0,0)
        elif board == 3:
            # 8x8 board without a few spots
            game_board_solution = [[random.choice(colors) for _ in range(8)] for _ in range(8)]
            for i in range(0, 8):
                for j in range(0, 8):
                    if i == 0 and j in [0, 4, 5, 6, 7]:
                        game_board_solution[i][j] = (0, 0, 0)
                    elif i == 1 and j in [3, 4, 5, 6, 7]:
                        game_board_solution[i][j] = (0, 0, 0)
                    elif i == 2 and j in [6, 7]:
                        game_board_solution[i][j] = (0, 0, 0)
                    elif i == 3 and j in [1, 3, 5, 6, 7]:
                        game_board_solution[i][j] = (0, 0, 0)
                    elif i == 4 and j in [0, 1]:
                        game_board_solution[i][j] = (0, 0, 0)
                    elif i == 5 and j in [0, 1, 3, 7]:
                        game_board_solution[i][j] = (0, 0, 0)
                    elif i == 6 and j in [0, 1, 2, 3, 6, 7]:
                        game_board_solution[i][j] = (0, 0, 0)
                    elif i == 7 and j in [0, 1, 2, 3, 5, 6, 7]:
                        game_board_solution[i][j] = (0, 0, 0)
            cursor_position = (0, 1)
        elif board == 4:
            # 6x6 square board
            game_board_solution = [[random.choice(colors) for _ in range(6)] for _ in range(6)]
        elif board == 5:
            # 8x8 razor board
            game_board_solution = [[(0,0,0) for _ in range(8)] for _ in range(8)]
            for i in range(8):
                for j in range(8):
                    if not ((i == 0 and j in [0, 1, 2, 3, 5, 6, 7]) or \
                    (i == 1 and j in [0, 1, 2, 7]) or \
                    (i == 2 and j in [0, 1, 5, 7]) or \
                    (i == 3 and j in [0, 4]) or \
                    (i == 4 and j in [3, 7]) or \
                    (i == 5 and j in [0, 2, 6, 7]) or \
                    (i == 6 and j in [0, 1, 5, 6, 7]) or \
                    (i == 7 and j in [0, 1, 2, 4, 5, 6, 7])):
                        game_board_solution[i][j] = random.choice(colors)
            cursor_position = (4,0)
        game_board_start = []
        for list in game_board_solution:
            game_board_start.append(list.copy())
        return game_board_start, game_board_solution, cursor_position

game_board_start, game_board_solution, cursor_position = generate_board(1)

game_board_start = regression_algorithm(cursor_position,game_board_start, 1)

# Copy the board
def copy(board):
    new_board = []
    for i in range(len(board)):
        temp = board[i].copy()
        new_board.append(temp)
    return new_board

# Convert list to tuple
def list_to_tuple(l):
    return tuple([tuple(x) for x in l])


class GameState:
    def __init__(self,cursor_position,board,goal_board,previous_move=START):
        self.cursor_position = cursor_position
        self.board = board
        self.goal_board = goal_board
        self.previous_move = previous_move
    
    # Check if the cursor positions and the boards are equal
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.cursor_position == self.cursor_position and other.board == self.board
        else:
            return False

    # Check if the cursor positions and the boards are not equal
    def __ne__(self, other):
        return not self.__eq__(other)
    
    # Creates the hash for the game state
    def __hash__(self):
        return hash((self.cursor_position, list_to_tuple(self.board)))

    # Convert the current position and the board to a string
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

    # Check if the position/move is valid
    def valid_move(pos,board):
        if(pos[0] < 0 or pos[0] >= len(board[0]) or pos[1] < 0 or pos[1] >= len(board)):
            return False
        return board[pos[1]][pos[0]] != (0,0,0)

    # Update the color of the position
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

    # Move the cursor up
    def up(state):
        new_cursor = (state.cursor_position[0],state.cursor_position[1]-1)
        if(not GameState.valid_move(new_cursor,state.board)):
            return state
        else:
            new_board = GameState.color_update(state.cursor_position,new_cursor,state.board)
            return GameState(new_cursor,new_board,state.goal_board,UP)
        
    # Move the cursor down
    def down(state):
        new_cursor = (state.cursor_position[0],state.cursor_position[1]+1)
        if(not GameState.valid_move(new_cursor,state.board)):
            return state
        else:
            new_board = GameState.color_update(state.cursor_position,new_cursor,state.board)
            return GameState(new_cursor,new_board,state.goal_board,DOWN)
    
    # Move the cursor left
    def left(state):
        new_cursor = (state.cursor_position[0]-1,state.cursor_position[1])
        if(not GameState.valid_move(new_cursor,state.board)):
            return state
        else:
            new_board = GameState.color_update(state.cursor_position,new_cursor,state.board)
            return GameState(new_cursor,new_board,state.goal_board,LEFT)
    
    # Move the cursor right
    def right(state):
        new_cursor = (state.cursor_position[0]+1,state.cursor_position[1])
        if(not GameState.valid_move(new_cursor,state.board)):
            return state
        else:
            new_board = GameState.color_update(state.cursor_position,new_cursor,state.board)
            return GameState(new_cursor,new_board,state.goal_board,RIGHT)
    
    # Get the possible states from the current one
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
    
    # Check if the current state is the goal state
    def goal_state(state):
        res = state.board == state.goal_board
        g = True
        for i in range(len(state.board)):
            for j in range(len(state.board[i])):
                if(state.board[i][j] != state.goal_board[i][j]):
                    g = False
            
        return g
    
    # Heuristic function to calculate the distance between the current state and the goal state
    def simple_heuristic(state):
        board = state.board
        goal_board = state.goal_board
        distance = 0

        for i in range(len(board)):
            for j in range(len(board[i])):
                if(board[i][j] != goal_board[i][j]):
                    distance += 1
        return distance
    
    # Heuristic function to calculate the distance between the current state and the goal state
    def color_clusters_heuristic(state):
        board = state.board
        goal = state.goal_board
        # Helper function to find connected components (clusters) using DFS
        def dfs(x, y, color):
            if not (0 <= x < 4 and 0 <= y < 4) or visited[x][y] or board[x][y] != color:
                return
            visited[x][y] = True
            for dx, dy in moves:
                dfs(x + dx, y + dy, color)

        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False] * 4 for _ in range(4)]
        clusters = 0

        # Count clusters in the current state
        for i in range(4):
            for j in range(4):
                if not visited[i][j]:
                    dfs(i, j, board[i][j])
                    clusters += 1

        # Count clusters in the goal state
        visited = [[False] * 4 for _ in range(4)]
        goal_clusters = 0
        for i in range(4):
            for j in range(4):
                if not visited[i][j]:
                    dfs(i, j, goal[i][j])
                    goal_clusters += 1

        # Calculate the difference in cluster counts between the current state and the goal state
        return abs(clusters - goal_clusters)
        
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

    # Add a child to the current node
    def add_child(self, child_node):
        self.children.append(child_node)
        child_node.parent = self
        child_node.depth = self.depth + 1

    # Breadth-first Search Algorithm
    def breadth_first_search(initial_state, goal_state_func, operators_func):
        root = TreeNode(initial_state)   # create the root node in the search tree
        queue = deque([root])   # initialize the queue to store the nodes
        while queue:
            node = queue.popleft()
            print("Depth: ", node.depth)
            if goal_state_func(node.state):
                return node
            else:
                new_states = operators_func(node.state)
                for state in new_states:
                    new_node = TreeNode(state)
                    node.add_child(new_node)
                    queue.append(new_node)
            
        return None
    
    # Depth-first Search Algorithm
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
    
    # Greedy Search Algorithm
    def greedy_search(initial_state, goal_state_func, operators_func, heuristic_func):
        root = TreeNode(initial_state)
        open_list = [root] # List of nodes to be visited
        closed_list = [] # List of visited nodes

        while open_list: 
            open_list.sort(key=lambda x: heuristic_func(x.state)) # Sort the open list based on the heuristic function
            node = open_list.pop(0)
            closed_list.append(node) # Add the current node to the visited list
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
    
    # A* Search Algorithm
    def a_star_search(initial_state, goal_state_func, operators_func, heuristic_func):
        root = TreeNode(initial_state)
        open_list = [root] # List of nodes to be visited
        closed_list = [] # List of visited nodes

        while open_list:
            open_list.sort(key=lambda x: heuristic_func(x.state) + x.depth) # Sort the open list based on the heuristic function and the depth of the node
            node = open_list.pop(0)
            closed_list.append(node) # Add the current node to the visited list
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
    
    # Depth-limited Search Algorithm
    def depth_limited_search(initial_state, goal_state_func, operators_func, depth_limit):
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

    # Iterative Deepening Search Algorithm
    def iterative_deepening_search(initial_state, goal_state_func, operators_func, max_depth):
        for depth in range(max_depth):
            print(depth)
            result = TreeNode.depth_limited_search(initial_state,goal_state_func,operators_func,depth) # Call depth limited search, increasing depth each time
            if result is not None:
                return result
        
        return None
    
    def sub_depth_limited_search(node, goal_state_func, operators_func, depth_limit):
        if goal_state_func(node.state): # Check if the current node is the goal state
            return node
        if node.depth == depth_limit: # Check if the current node is at the depth limit of the search
            return None
        for state in operators_func(node.state):
            child_node = TreeNode(state=state, parent=node) # Create a child node from the current node
            result = TreeNode.sub_depth_limited_search(child_node, goal_state_func, operators_func, depth_limit) # Recursively call the function on the child node
            if result is not None:
                return result
        return None

    # Print the solution
    def print_solution(node):
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
    
    # Get the path
    def get_path(node):
        if node:
            path = []
            while node:
                path.append(node)
                node = node.parent
            return path
        return None
    
"""  
    def ida_star_search(initial_state, goal_state_func, operators_func, heuristic_func, max_depth):
        depth = heuristic_func(initial_state)
        while depth <= max_depth:
            result = 1
            if result is not None:
                return result
        return None
"""