import random

main_list = ['mechanical', 'plasma']

all_animals = ['amphibian', 'reptile', 'bird', 'shark', 'lion', 'wolf', 'bear',
               'human', 'bat', 'rhinoceroses', 'kangaroo', 'rabbit', 'worm', 'snake', 'insect', 'arachnid', 'dragon', 'pig', 'horse', 'elephant']

features = {
    # body
    'body_type': all_animals,
    'body_size': ['xs', 'sm', 'md', 'lg', 'xl', 'xxl'],

    'skin_type': ['amphibian', 'scales', 'exoskeleton',
                  'dermal denticles', 'fur', 'human', 'feathers'] + main_list,

    # appendages
    'wing_type': ['none', 'dragon', 'bird', 'bat', 'insect'] + main_list,
    'num_wings': [0, 2, 4, 6, 8],

    # do for left and right
    'arm_type': ['none', 'amphibian', 'reptile',
                 'human', 'horse', 'dog', 'bear', 'fin', 'rhinoceroses', 'kangaroo', 'arachnid', 'rabbit', 'insect', 'tenticle'] + main_list,
    'num_arms': [0, 2, 4, 6, 8],

    # do for left and right
    'leg_type': ['none', 'amphibian', 'reptile',
                 'human', 'horse', 'dog', 'bear', 'fin', 'rhinoceroses', 'kangaroo', 'arachnid', 'rabbit', 'insect', 'tenticle'] + main_list,
    'num_legs': [0, 2, 4, 6, 8],

    'tail_type': ['none', 'amphibian', 'reptile', 'horse', 'dog', 'cat', 'fin', 'rhinoceroses', 'kangaroo', 'arachnid', 'rabbit', 'insect'],
    'num_tails': [0, 1, 2, 3, 4, 5, 6],

    'neck_length': ['none', 'human', 'horse', 'giraffe', 'ostrich'],

    # head
    'eye_type': ['none', 'amphibian', 'reptile',
                 'human', 'arachnid', 'insect', 'squid', 'shark', 'wolf', 'horse'] + main_list,
    'num_eyes': [0, 1, 2, 3, 4, 5, 6],

    'mouth_type': all_animals + ['none'],

    'head_top_feature_type': ['fin', 'hair', 'none', 'antenna'],

    'nose_type': all_animals + ['none'],

    'ear_type': all_animals + ['none']
}

for feature in features.items():
    print(f"{feature[0]}: {random.choice(feature[1])}")
