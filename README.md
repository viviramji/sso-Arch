# Single Sign On (SSO)

Inicio de sesión único (SSO) hace referencia a cuando un usuario inicia sesión en una aplicación con un único conjunto de credenciales y, a continuación, inicia sesión automáticamente en varias aplicaciones. Con el inicio de sesión SSO, un usuario obtiene acceso a varios sistemas de software sin mantener diferentes credenciales de inicio de sesión, como nombres de usuario y contraseñas.

Por ejemplo, en el caso de Google con sus diferentes productos, cuando un usuario ingresa a su Gmail, el usuario automáticamente tiene acceso a Youtube, Google Drive, Photos, entre otros productos de Google.

![SSO Graph](images/sso-arch.jpg)

## Diagrama de flujo de una arquitectura típica de SSO

![Arquitectura típica de SSO](images/typical-sso.png)

1. El usuario navega al Flaskr (aplicación 1). 
2. Redirecciona al Auth server (controlador).   
3. En Auth Server se comprueba si ya se realizó la autenticación del usuario. En este caso, el usuario debe proporcionar su usuario y contraseña. 
4. Auth Sever busca información de sesión del usuario, la cual no fue encontrada, por lo que en el punto 3 se pidieron los datos. 
5. Flaskr (aplicación 1) recibe información de la aurtenticación del usuario por parte de Auth Server. 
6. Flaskr (aplicación 1) usa el objeto sesión proveniente de Auth Server (Controlador) y permite el ingreso del usuario al aplicativo. 
7. Se guarda la información relacionada con el acceso del usuario al aplicativo 1. Esta información será consultada cuando el usuario desee ingresar a otra aplicación vinculada, en este caso, app2. 
8. El usuario se dirige a app2.com. 
9. app2.com se comunica con Auth Server, en orden de realizar la autenticación del usuario. 
10. Auth Server se encarga de consultar información acerca de la sesión del usuario. En este caso, el usuario ya había proporcionado sus datos de ingreso en app1, por lo que no se le solicitan nuevamente. 
11. Auth Server envía información del objeto sesión a app2. 
12. App2.com permite ingresar al usuario. 
13. Se guarda la información relacionada con el acceso del usuario al aplicativo 2.  

## Pasos para correr el proyecto

Estructura del repo

```
sso-arch
│    README.md
└─── images/...
│   
└─── app1
│   │   flask app
│   │   ...
│   
└─── app2
│    │   flask app
│    │   ...
│
└─── auth-server
     │  flask app
     │  ...   
    
```

## Referencias

* [SSO Login: Key Benefits and Implementation](https://dzone.com/articles/sso-login-key-benefits-and-implementation)
