from typing import Callable, Any
from flask import session, redirect, url_for
# from functools import wraps


def login_required(func:Callable[..., Any]) -> Callable[..., Any]:
    # @wraps
    def wraped(*args,**kwargs):
        if not session.get("user"):
           return redirect(url_for("login"))

        return func(*args, **kwargs)
    
    return wraped
    
