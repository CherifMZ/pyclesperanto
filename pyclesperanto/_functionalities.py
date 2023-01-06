from ._memory_operations import pull
from typing import Optional, Union


def imshow(
    image,
    title: Optional[str] = None,
    labels: Optional[bool] = False,
    min_display_intensity: Optional[float] = None,
    max_display_intensity: Optional[float] = None,
    color_map: Optional[str]=None,
    plot=None,
    colorbar: Optional[bool] = False,
    colormap: Union[str, None] = None,
    alpha: Optional[float] = None,
    continue_drawing: Optional[bool] = False,
):
    """Visualize an image, e.g. in Jupyter notebooks.
    Parameters
    ----------
    image: np.ndarray
        numpy or OpenCL-backed image to visualize
    title: str, optional
        Obsolete (kept for ImageJ-compatibility)
    labels: bool, optional
        True: integer labels will be visualized with colors
        False: Specified or default colormap will be used to display intensities.
    min_display_intensity: float, optional
        lower limit for display range
    max_display_intensity: float, optional
        upper limit for display range
    color_map: str, optional
        deprecated, use colormap instead
    plot: matplotlib axis, optional
        Plot object where the image should be shown. Useful for putting multiple images in subfigures.
    colorbar: bool, optional
        True puts a colorbar next to the image. Will not work with label images and when visualizing multiple
        images (continue_drawing=True).
    colormap: str or matplotlib colormap, optional
    alpha: float, optional
        alpha blending value
    continue_drawing: float
        True: the next shown image can be visualized on top of the current one, e.g. with alpha = 0.5
    """
    import numpy as np

    if not isinstance(image, np.ndarray):
        image = pull(image)

    if len(image.shape) == 3:
        from ._tier1 import maximum_z_projection

        image = pull(maximum_z_projection(image))

    if color_map is not None:
        import warnings

        warnings.warn(
            "The imshow parameter color_map is deprecated. Use colormap instead."
        )
        if colormap is None:
            colormap = color_map

    if colormap is None:
        colormap = "Greys_r"

    cmap = colormap
    if labels:
        import matplotlib
        import numpy as np

        # if not hasattr("labels_cmap"):
        from numpy.random import MT19937
        from numpy.random import RandomState, SeedSequence

        rs = RandomState(MT19937(SeedSequence(3)))
        lut = rs.rand(65537, 3)
        lut[0, :] = 0
        labels_cmap = matplotlib.colors.ListedColormap(lut)
        cmap = labels_cmap

        if min_display_intensity is None:
            min_display_intensity = 0

    if plot is None:
        import matplotlib.pyplot as plt

        plt.imshow(
            image,
            cmap=cmap,
            vmin=min_display_intensity,
            vmax=max_display_intensity,
            interpolation="nearest",
            alpha=alpha,
        )
        if colorbar:
            plt.colorbar()
        if not continue_drawing:
            plt.show()
    else:
        plot.imshow(
            image,
            cmap=cmap,
            vmin=min_display_intensity,
            vmax=max_display_intensity,
            interpolation="nearest",
            alpha=alpha,
        )
        if colorbar:
            plot.colorbar()
    if title is not None:
        plt.title(title)
