# recent/functions.py

"""
Example:
    
    def form_valid(self, form):
        messages.success(self.request, 'Changes saved!')
        log_form_valid(self, form)
        return super(ThingUpdateView, self).form_valid(form)

"""

from .models import Log

def log_form_valid(s, form):
    """
    Put near the end of a form_valid override and call like this:
        log_form_valid(self, form)
    
    Really only useful on generic UpdateView and CreateView classes.
    """
    #
    # 
    try:
        user_name = s.request.user
    except AttributeError:
        user_name = ''
    except Exception as e:
        user_name = e
    #
    # I don't think these should ever
    # actually fail, but if they do
    # then log it. 
    try:
        model_name = s.model.__name__
    except Exception as e:
        model_name = e
    try:
        view_name = s.__class__.__name__
    except Exception as e:
        view_name = e
    #
    try:
        object_name = s.object.name
    except Exception:
        try:
            object_name = s.request.POST.get('name').lower()
        except Exception as e:
            object_name = e
    #
    # 
    try:
        post = ''
        for k,v in s.request.POST.items():
            if 'middlewaretoken' not in k:
                post += '\n{} => "{}"\n'.format(k,v)
    except Exception as e:
        post = e
    #
    #
    if 'UpdateView' in view_name:
        model_name = model_name.replace('UpdateView','').lower()
        view_name = 'changed'
    
    if 'CreateView' in view_name:
        model_name = model_name.replace('CreateView','').lower()
        view_name = 'created'
    #
    D_B = Log(
        user=user_name,
        view_name=view_name,
        model_name=model_name,
        object_name=object_name,
        verbose=post,
        )
    D_B.save()
