

# python manage.py rqworker --worker-class videoflix.windows_worker.WindowsWorker


from rq import Worker

class WindowsWorker(Worker):

    def store_job(self, job, queue):
        print(f"Storing job {job.id} in queue {queue.name}")
       

    def execute_job(self, job, queue):
        self.store_job(job, queue=queue)
        result = self.perform_job(job, queue=queue)
        return result

    def perform_job(self, job, queue):
        try:
            job.perform()
            job.status = 'finished'
            print(f"Job {job.id} finished successfully.")
            return True
        except Exception as e:
            job.status = 'failed'
            print(f"Job {job.id} failed with error: {str(e)}")
            return False
