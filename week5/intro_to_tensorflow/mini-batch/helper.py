import math
def batches(batch_size, features, labels):
    """
    Create batches of features and labels
    :param batch_size: The batch size
    :param features: List of features
    :param labels: List of labels
    :return: Batches of (Features, Labels)
    """
    assert len(features) == len(labels)
    # TODO: Implement batching
    mini_batches = []
    
    for i in range(len(features)):
        if i % batch_size == 0:
            mini_batches.append([
                features[i:i+batch_size],
                labels[i:i+batch_size]
            ])
    
    return mini_batches
