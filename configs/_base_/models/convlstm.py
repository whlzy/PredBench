num_hidden = [128,128,128,128]
filter_size = 5
stride = 1
patch_size = 2
layer_norm = 0


RNN=dict(
    type='ConvLSTM',
    input_shape=(10, 3, 64, 64),    # (T, C, H, W)
    num_layers=len(num_hidden), 
    num_hidden=num_hidden, 
    patch_size=patch_size, 
    filter_size=filter_size, 
    stride=stride, 
    layer_norm=layer_norm, 
)  