import multiprocessing

bind='0.0.0.0:8082'   
workers=multiprocessing.cpu_count() + 1            
backlog=2048            
worker_class="gevent" 
max_requests=1000       
daemon=False           
reload=True            
pidfile='./app_2.gunicorn.pid'    
loglevel='debug'     
accesslog='log/app_2.gunicorn.log'  
errorlog='log/app_2.gunicorn.err.log' 