"""
Centralized logging infrastructure for DADBOT v4
Provides debug logging to help diagnose issues
"""

import logging
import sys
from pathlib import Path
from datetime import datetime

# Global logger instance
_logger = None


def setup_logger(name="DADBOT", log_level=logging.DEBUG):
    """
    Set up centralized logger for the application
    
    Args:
        name: Logger name
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    
    Returns:
        Logger instance
    """
    global _logger
    
    if _logger is not None:
        return _logger
    
    _logger = logging.getLogger(name)
    _logger.setLevel(log_level)
    
    # Prevent duplicate handlers
    if _logger.handlers:
        return _logger
    
    # File handler - logs to app_debug.log in project root
    log_file = Path(__file__).parent.parent.parent / "app_debug.log"
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    
    # Console handler - only show warnings and above
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.WARNING)
    
    # Formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    _logger.addHandler(file_handler)
    _logger.addHandler(console_handler)
    
    _logger.info("=" * 60)
    _logger.info(f"DADBOT v4 Logging initialized at {datetime.now()}")
    _logger.info("=" * 60)
    
    return _logger


def get_logger():
    """Get the global logger instance, creating it if needed"""
    global _logger
    if _logger is None:
        _logger = setup_logger()
    return _logger


def log_exception(exception, context=""):
    """
    Log an exception with context
    
    Args:
        exception: The exception object
        context: Additional context string describing where/why the exception occurred
    """
    logger = get_logger()
    if context:
        logger.error(f"{context}: {type(exception).__name__}: {str(exception)}", exc_info=True)
    else:
        logger.error(f"{type(exception).__name__}: {str(exception)}", exc_info=True)


def log_widget_error(widget_name, operation, exception):
    """
    Log widget-related errors
    
    Args:
        widget_name: Name of the widget
        operation: What operation was being performed
        exception: The exception that occurred
    """
    logger = get_logger()
    logger.error(f"Widget '{widget_name}' - {operation}: {type(exception).__name__}: {str(exception)}")


def log_connection_error(source, signal, target, exception):
    """
    Log signal/slot connection errors
    
    Args:
        source: Source widget/object name
        signal: Signal name
        target: Target handler name
        exception: The exception that occurred
    """
    logger = get_logger()
    logger.error(f"Connection failed: {source}.{signal} -> {target}: {type(exception).__name__}: {str(exception)}")
