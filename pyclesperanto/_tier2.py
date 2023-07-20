
# this code is auto-generated by the script 'pyclesperanto_autogen_tier_script.ipynb'.
# Do not edit manually. Instead, edit the script and run it again.

from ._core import Device
from ._array import Image
from ._decorators import plugin_function


@plugin_function
def absolute_difference(
    input_image0: Image,
	input_image1: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _absolute_difference as op
    
    return op(
        device=device,
		src0=input_image0,
		src1=input_image1,
		dst=output_image
    )


@plugin_function
def add_images(
    input_image0: Image,
	input_image1: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _add_images as op
    
    return op(
        device=device,
		src0=input_image0,
		src1=input_image1,
		dst=output_image
    )


@plugin_function
def bottom_hat_box(
    input_image: Image,
	output_image: Image = None,
	radius_x: int = 0,
	radius_y: int = 0,
	radius_z: int = 0,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _bottom_hat_box as op
    
    return op(
        device=device,
		src=input_image,
		dst=output_image,
		radius_x=int(radius_x),
		radius_y=int(radius_y),
		radius_z=int(radius_z)
    )


@plugin_function
def bottom_hat_sphere(
    input_image: Image,
	output_image: Image = None,
	radius_x: float = 0,
	radius_y: float = 0,
	radius_z: float = 0,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _bottom_hat_sphere as op
    
    return op(
        device=device,
		src=input_image,
		dst=output_image,
		radius_x=float(radius_x),
		radius_y=float(radius_y),
		radius_z=float(radius_z)
    )


@plugin_function
def clip(
    input_image: Image,
	output_image: Image = None,
	min_intensity: float = 0,
	max_intensity: float = 0,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _clip as op
    
    return op(
        device=device,
		src=input_image,
		dst=output_image,
		min_intensity=float(min_intensity),
		max_intensity=float(max_intensity)
    )


@plugin_function
def closing_box(
    input_image: Image,
	output_image: Image = None,
	radius_x: int = 0,
	radius_y: int = 0,
	radius_z: int = 0,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _closing_box as op
    
    return op(
        device=device,
		src=input_image,
		dst=output_image,
		radius_x=int(radius_x),
		radius_y=int(radius_y),
		radius_z=int(radius_z)
    )


@plugin_function
def closing_sphere(
    input_image: Image,
	output_image: Image = None,
	radius_x: float = 0,
	radius_y: float = 0,
	radius_z: float = 0,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _closing_sphere as op
    
    return op(
        device=device,
		src=input_image,
		dst=output_image,
		radius_x=float(radius_x),
		radius_y=float(radius_y),
		radius_z=float(radius_z)
    )


@plugin_function
def degrees_to_radians(
    input_image: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _degrees_to_radians as op
    
    return op(
        device=device,
		src=input_image,
		dst=output_image
    )


@plugin_function
def difference_of_gaussian(
    input_image: Image,
	output_image: Image = None,
	sigma1_x: float = 0,
	sigma1_y: float = 0,
	sigma1_z: float = 0,
	sigma2_x: float = 0,
	sigma2_y: float = 0,
	sigma2_z: float = 0,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _difference_of_gaussian as op
    
    return op(
        device=device,
		src=input_image,
		dst=output_image,
		sigma1_x=float(sigma1_x),
		sigma1_y=float(sigma1_y),
		sigma1_z=float(sigma1_z),
		sigma2_x=float(sigma2_x),
		sigma2_y=float(sigma2_y),
		sigma2_z=float(sigma2_z)
    )


@plugin_function
def invert(
    input_image: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _invert as op
    
    return op(
        device=device,
		src=input_image,
		dst=output_image
    )


@plugin_function
def label_spots(
    input_image: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _label_spots as op
    
    return op(
        device=device,
		src=input_image,
		dst=output_image
    )


@plugin_function
def maximum_of_all_pixels(
    input_image: Image,
	device: Device = None
) -> float:
    from ._pyclesperanto import _maximum_of_all_pixels as op
    
    return op(
        device=device,
		src=input_image
    )


@plugin_function
def minimum_of_all_pixels(
    input_image: Image,
	device: Device = None
) -> float:
    from ._pyclesperanto import _minimum_of_all_pixels as op
    
    return op(
        device=device,
		src=input_image
    )


@plugin_function
def opening_box(
    input_image: Image,
	output_image: Image = None,
	radius_x: int = 0,
	radius_y: int = 0,
	radius_z: int = 0,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _opening_box as op
    
    return op(
        device=device,
		src=input_image,
		dst=output_image,
		radius_x=int(radius_x),
		radius_y=int(radius_y),
		radius_z=int(radius_z)
    )


@plugin_function
def opening_sphere(
    input_image: Image,
	output_image: Image = None,
	radius_x: float = 0,
	radius_y: float = 0,
	radius_z: float = 0,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _opening_sphere as op
    
    return op(
        device=device,
		src=input_image,
		dst=output_image,
		radius_x=float(radius_x),
		radius_y=float(radius_y),
		radius_z=float(radius_z)
    )


@plugin_function
def radians_to_degrees(
    input_image: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _radians_to_degrees as op
    
    return op(
        device=device,
		src=input_image,
		dst=output_image
    )


@plugin_function
def square(
    input_image: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _square as op
    
    return op(
        device=device,
		src=input_image,
		dst=output_image
    )


@plugin_function
def squared_difference(
    input_image0: Image,
	input_image1: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _squared_difference as op
    
    return op(
        device=device,
		src0=input_image0,
		src1=input_image1,
		dst=output_image
    )


@plugin_function
def subtract_images(
    input_image0: Image,
	input_image1: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _subtract_images as op
    
    return op(
        device=device,
		src0=input_image0,
		src1=input_image1,
		dst=output_image
    )


@plugin_function
def sum_of_all_pixels(
    input_image: Image,
	device: Device = None
) -> float:
    from ._pyclesperanto import _sum_of_all_pixels as op
    
    return op(
        device=device,
		src=input_image
    )


@plugin_function
def top_hat_box(
    input_image: Image,
	output_image: Image = None,
	radius_x: int = 0,
	radius_y: int = 0,
	radius_z: int = 0,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _top_hat_box as op
    
    return op(
        device=device,
		src=input_image,
		dst=output_image,
		radius_x=int(radius_x),
		radius_y=int(radius_y),
		radius_z=int(radius_z)
    )


@plugin_function
def top_hat_sphere(
    input_image: Image,
	output_image: Image = None,
	radius_x: float = 0,
	radius_y: float = 0,
	radius_z: float = 0,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _top_hat_sphere as op
    
    return op(
        device=device,
		src=input_image,
		dst=output_image,
		radius_x=float(radius_x),
		radius_y=float(radius_y),
		radius_z=float(radius_z)
    )

