from ._image import Image
from ._device import Device
from ._decorators import plugin_function


@plugin_function
def masked_voronoi_labeling(
    input_image: Image,
    mask_image: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    """Takes a binary image, labels connected components and dilates the
    regions using a octagon shape until they touch. The region growing is limited to a masked area.

    The resulting label map is written to the output.

    Parameters
    ----------
    input_image : Image
        The input binary image.
    mask_image : Image
        The mask image.
    output_image : Image, optional
        The output label map.
    device: Device, optional
        The device to be used for computation.

    Returns
    -------
    output_image : Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_maskedVoronoiLabeling
    """
    from ._pyclesperanto import _MaskedVoronoiLabelingKernel_Call as op

    op(device, src=input_image, dst=output_image, mask=mask_image)
    return output_image
