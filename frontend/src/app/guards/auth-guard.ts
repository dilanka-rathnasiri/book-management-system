import { inject } from '@angular/core';
import { CanActivateFn, Router } from '@angular/router';
import { AuthServices } from '../services/auth-services';

export const authGuard: CanActivateFn = (route, state) => {
  const router = inject(Router);
  const authService = inject(AuthServices);

  if (authService.isAuthenticated()) {
    return true;
  }

  // No valid token, redirect to login
  router.navigate(['/login']);
  return false;
};
