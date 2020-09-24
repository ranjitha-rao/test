import queue


class Node:

    def __init__(self, info):
        '''Constructor'''
        self.info = info
        self.children = []
        self.level = None
        self.parent = None

    def __str__(self):
        return str(self.info)

    def display_tree(self, level=0):
        '''Displaying the hierarchical result '''
        tabs_level = "\t" * level
        print(f'{tabs_level}{self.info}\n')
        for child in self.children:
            # Recursively display all children
            child.display_tree(level + 1)

    @staticmethod
    def create_node(family_member : str):
        '''Helper method to create a node'''
        member_data = family_member.split(sep=',')
        current_node =  Node(member_data[2])
        current_node.level = member_data[1]
        # Root does not have a parent
        current_node.parent = member_data[0] if member_data[0].isdigit() else None
        return current_node

    @staticmethod
    def create_family_tree(input_string:str):
        '''Creaet family tree'''
        family = input_string.split(sep='|')
        parent_queue = queue.Queue()
        cur_parent = None
        root = None
        for family_member in family:
            # create the node
            node = Node.create_node(family_member)
            # Put it in a queue.
            parent_queue.put(node)
            if not node.parent:
                # No parent must be the root
                root = node
                # root is now the cur_parent
                cur_parent = parent_queue.get()
                continue
            while cur_parent.level and cur_parent.level != node.parent:
                # Keep popping from the queue, until you find the parent.
                cur_parent = parent_queue.get()
            if cur_parent.level == node.parent:
                # Found parent child pair
                cur_parent.children.append(node)
        return root

if __name__ == '__main__':
   # root = Node.create_family_tree(input_string = "None,0,grandpa|0,1,son|0,2,daugther|1,3,grandkid|1,4,grandkid|2,5,grandkid|5,6,greatgrandkid")
    root = Node.create_family_tree(input_string="None,0,Smith|0,1,Conor|0,2,Cooper|1,3,Alexis|1,4,Sue|2,5,Max|2,6,Elvis|2,7,Steven|3,8,Joe|5,9,Luis|8,10,Clark")
    print(root.display_tree())



