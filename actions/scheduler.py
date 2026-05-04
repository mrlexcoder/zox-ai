"""
Task Scheduler - Schedule tasks to run at specific times
Uses schedule library for simple scheduling
"""

import schedule
import time
import logging
import threading
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TaskScheduler:
    """Schedule and manage tasks"""
    
    def __init__(self):
        self.tasks = []
        self.running = False
        self.scheduler_thread = None
    
    def schedule_task(self, time_str, command, task_name=None):
        """
        Schedule a task to run at a specific time
        time_str: time in format "HH:MM" (e.g., "14:30")
        command: command to execute (string or callable)
        task_name: optional name for the task
        """
        try:
            if task_name is None:
                task_name = f"Task_{len(self.tasks) + 1}"
            
            logger.info(f"Scheduling task '{task_name}' at {time_str}")
            
            # Schedule the task
            job = schedule.every().day.at(time_str).do(self._execute_task, command, task_name)
            
            self.tasks.append({
                'name': task_name,
                'time': time_str,
                'command': command,
                'job': job
            })
            
            # Start scheduler thread if not running
            if not self.running:
                self.start()
            
            return True
            
        except Exception as e:
            logger.error(f"Error scheduling task: {str(e)}")
            return False
    
    def schedule_recurring(self, interval, unit, command, task_name=None):
        """
        Schedule a recurring task
        interval: number of units
        unit: 'seconds', 'minutes', 'hours', 'days', 'weeks'
        command: command to execute
        task_name: optional name for the task
        """
        try:
            if task_name is None:
                task_name = f"Recurring_{len(self.tasks) + 1}"
            
            logger.info(f"Scheduling recurring task '{task_name}' every {interval} {unit}")
            
            # Create schedule based on unit
            if unit == 'seconds':
                job = schedule.every(interval).seconds.do(self._execute_task, command, task_name)
            elif unit == 'minutes':
                job = schedule.every(interval).minutes.do(self._execute_task, command, task_name)
            elif unit == 'hours':
                job = schedule.every(interval).hours.do(self._execute_task, command, task_name)
            elif unit == 'days':
                job = schedule.every(interval).days.do(self._execute_task, command, task_name)
            elif unit == 'weeks':
                job = schedule.every(interval).weeks.do(self._execute_task, command, task_name)
            else:
                raise ValueError(f"Invalid unit: {unit}")
            
            self.tasks.append({
                'name': task_name,
                'interval': interval,
                'unit': unit,
                'command': command,
                'job': job
            })
            
            # Start scheduler thread if not running
            if not self.running:
                self.start()
            
            return True
            
        except Exception as e:
            logger.error(f"Error scheduling recurring task: {str(e)}")
            return False
    
    def _execute_task(self, command, task_name):
        """Execute a scheduled task"""
        try:
            logger.info(f"Executing task: {task_name}")
            
            if callable(command):
                # Execute function
                command()
            else:
                # Execute command string
                import subprocess
                subprocess.run(command, shell=True)
            
            logger.info(f"Task '{task_name}' completed")
            
        except Exception as e:
            logger.error(f"Error executing task '{task_name}': {str(e)}")
    
    def start(self):
        """Start the scheduler thread"""
        if self.running:
            logger.warning("Scheduler already running")
            return
        
        self.running = True
        self.scheduler_thread = threading.Thread(target=self._run_scheduler, daemon=True)
        self.scheduler_thread.start()
        logger.info("Scheduler started")
    
    def stop(self):
        """Stop the scheduler thread"""
        self.running = False
        if self.scheduler_thread:
            self.scheduler_thread.join(timeout=2)
        logger.info("Scheduler stopped")
    
    def _run_scheduler(self):
        """Run the scheduler loop"""
        while self.running:
            schedule.run_pending()
            time.sleep(1)
    
    def list_tasks(self):
        """
        List all scheduled tasks
        Returns: list of task info dicts
        """
        return [
            {
                'name': task['name'],
                'time': task.get('time'),
                'interval': task.get('interval'),
                'unit': task.get('unit'),
                'next_run': task['job'].next_run
            }
            for task in self.tasks
        ]
    
    def cancel_task(self, task_name):
        """
        Cancel a scheduled task by name
        task_name: name of task to cancel
        """
        try:
            for i, task in enumerate(self.tasks):
                if task['name'] == task_name:
                    schedule.cancel_job(task['job'])
                    self.tasks.pop(i)
                    logger.info(f"Cancelled task: {task_name}")
                    return True
            
            logger.warning(f"Task not found: {task_name}")
            return False
            
        except Exception as e:
            logger.error(f"Error cancelling task: {str(e)}")
            return False
    
    def cancel_all_tasks(self):
        """Cancel all scheduled tasks"""
        try:
            schedule.clear()
            self.tasks.clear()
            logger.info("Cancelled all tasks")
            return True
        except Exception as e:
            logger.error(f"Error cancelling all tasks: {str(e)}")
            return False
    
    def get_next_run_time(self, task_name):
        """
        Get the next run time for a task
        task_name: name of task
        Returns: datetime object or None
        """
        for task in self.tasks:
            if task['name'] == task_name:
                return task['job'].next_run
        return None


# Example task functions
def example_task():
    """Example task function"""
    print(f"Task executed at {datetime.now()}")


def reminder_task(message):
    """Example reminder task"""
    print(f"REMINDER: {message}")


if __name__ == "__main__":
    # Test scheduler
    scheduler = TaskScheduler()
    
    print("Testing task scheduler...")
    
    # Schedule a task for 5 seconds from now
    print("\nScheduling task in 5 seconds...")
    scheduler.schedule_recurring(5, 'seconds', example_task, 'test_task')
    
    # List tasks
    print("\nScheduled tasks:")
    for task in scheduler.list_tasks():
        print(f"  {task['name']}: next run at {task['next_run']}")
    
    # Wait for task to run
    print("\nWaiting for task to run...")
    time.sleep(10)
    
    # Cancel task
    print("\nCancelling task...")
    scheduler.cancel_task('test_task')
    
    # Stop scheduler
    scheduler.stop()
    
    print("\nDone!")
