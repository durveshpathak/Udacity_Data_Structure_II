class Group(object):

    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user_name, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    if user_name in group.get_users():
        return True

    if len(group.get_groups()) == 0:
        return False
    else:
        for group_name in group.get_groups():
            result = is_user_in_group(user_name, group_name)

    return result






parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print(is_user_in_group('sub_child_user',sub_child))
    # True
print(is_user_in_group(user_name='child_user', group=parent))
    # False
print(is_user_in_group(user_name='sub_child_user', group=parent))
    # True
print(is_user_in_group(user_name='parent_user', group=parent))
    # False

print(is_user_in_group(user_name='', group=parent))
    # False
print(is_user_in_group(user_name='', group=child))
    # False