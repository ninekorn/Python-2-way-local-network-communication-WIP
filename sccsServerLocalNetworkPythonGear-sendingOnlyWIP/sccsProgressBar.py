#https://stackoverflow.com/questions/41707229/tqdm-printing-to-newline
-------------------------------------------
def ybar(progr, total, step=50):
    #starts with 1
    l2=(progr/total)//(1/step)
    if progr==1: print(f'[{total}]: '+'|'*int(l2), end = '') 
    else:
        l1=((progr-1)/total)//(1/step) 

        ll=int(l2-l1)
        if l1 < l2: 

            for j in range(1,ll+1):
                if (int(l1)+j)%5==0:
                    print('*', end = '')
                else:
                    print('|', end = '')
        if progr==total: print("  DONE")
        
        
for i in range(1,101):
    ybar(i,len(range(1,101)),50)
-------------------------------------------
    
    
    
-------------------------------------------
def foo_():
    time.sleep(0.3)

range_ = range(0, 10)
total = len(bytes_read)
with tqdm.tqdm(total=total, position=0, leave=True) as pbar:
   for i in tqdm.tqdm((foo_, range_ ), position=0, leave=True):
    pbar.update()
-------------------------------------------


#https://stackoverflow.com/questions/3160699/python-progress-bar
#pip install progressbar2
#easy_install progressbar2
#Or download the latest release from Pypi download here (https://pypi.python.org/pypi/progressbar2) or Github
#Note that the releases on Pypi are signed with my GPG key (https://pgp.mit.edu/pks/lookup?op=vindex&search=0xE81444E9CE1F695D) and can be checked using GPG:
#gpg –verify progressbar2-<version>.tar.gz.asc progressbar2-<version>.tar.gz
-------------------------------------------
import time
import sys

toolbar_width = 40

# setup toolbar
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

for i in xrange(toolbar_width):
    time.sleep(0.1) # do real work here
    # update the bar
    sys.stdout.write("-")
    sys.stdout.flush()

sys.stdout.write("]\n") # this ends the progress bar
-------------------------------------------

#https://stackoverflow.com/questions/3160699/python-progress-bar
-------------------------------------------
for i in tqdm.tqdm(bytes_read):
    time.sleep(10)
-------------------------------------------

    
    
    
    
    
    
