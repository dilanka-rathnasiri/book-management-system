import { HttpInterceptorFn } from '@angular/common/http';
import { inject } from '@angular/core';
import { AuthServices } from '../services/auth-services';

export const authInterceptor: HttpInterceptorFn = (req, next) => {
    const authServices = inject(AuthServices);

    // skip auth request
    if (req.url === '/auth/validate') {
        return next(req);
    }

    if (authServices.isAuthenticated()) {
        const reqWithToken = req.clone({
            headers: req.headers.set('Authorization', `Bearer ${authServices.bearerToken()}`),
        });
        return next(reqWithToken);
    }

    return next(req);
};
