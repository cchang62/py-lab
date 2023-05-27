import multiprocessing

bind='0.0.0.0:8081'   
workers=multiprocessing.cpu_count() + 1           
backlog=2048            
worker_class="gevent" 
max_requests=1000       
daemon=True           
reload=True            
pidfile='./app_1.gunicorn.pid'    
loglevel='debug'     
accesslog='log/app_1.gunicorn.log'  
errorlog='log/app_1.gunicorn.err.log' 