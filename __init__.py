import os
import streamlit.components.v1 as components

_COMPONENT_NAME = "streamlit-lightweight-charts"
_RELEASE = False

if not _RELEASE:
    _component_func = components.declare_component(
        _COMPONENT_NAME,
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend","build")
    _component_func = components.declare_component(_COMPONENT_NAME, path=build_dir)


# Create a wrapper function for the component. This is an optional
# best practice - we could simply expose the component function returned by
# `declare_component` and call it done. The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.
def streamlit_lightweight_charts(name, key=None):
    """Create a new instance of "streamlit_lightweight_charts".

    Parameters
    ----------
    name: str
        The name of the thing we're saying hello to. The component will display
        the text "Hello, {name}!"
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    int
        The number of times the component's "Click Me" button has been clicked.
        (This is the value passed to `Streamlit.setComponentValue` on the
        frontend.)

    """
    # Call through to our private component function. Arguments we pass here
    # will be sent to the frontend, where they'll be available in an "args"
    # dictionary.
    #
    # "default" is a special argument that specifies the initial return
    # value of the component before the user has interacted with it.
    component_value = _component_func(name=name, key=key, default=0)
    return component_value


# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run streamlit_lightweight_charts/__init__.py`
if not _RELEASE:
    import streamlit as st

    st.subheader("Component with constant args")
    num_clicks = streamlit_lightweight_charts("World")
    st.markdown("You've clicked %s times!" % int(num_clicks))

    st.markdown("---")

    st.subheader("Component with variable args")
    name_input = st.text_input("Enter a name", value="Streamlit")
    num_clicks = streamlit_lightweight_charts(name_input, key="foo")
    st.markdown("You've clicked %s times!" % int(num_clicks))
