# utilities/mixs.py

# core/custom Mixins

class RenderdataMixin(object):
    """
    Allow a CBV to set dictionary named 'renderdata' to be passed
    to the template it renders. OK if renderdata not set/used.
    """
    renderdata = {}

    def get_context_data(self, **kwargs):
        kwargs = super(RenderdataMixin, self).get_context_data(**kwargs)
        kwargs.update({"renderdata": self.get_renderdata()})
        return kwargs

    def get_renderdata(self):
        return self.renderdata
