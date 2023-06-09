#include "lists.h"
#include "/usr/include/python3.4/Python.h"
#include "/usr/include/python3.4/listobject.h"
#include "/usr/include/python3.4/object.h"

/**
 * print_python_list_info - prints python lists information
 * @p: Pointer to the Python object.
 *
 * Return:void.
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;
	Py_ssize_t item;
	PyObject *itemObj;
	const char *itemType;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (item = 0; item < size; item++)
	{
		itemObj = PyList_GetItem(p, item);
		itemType = Py_TYPE(itemObj)->tp_name;
		printf("Element %ld: %s\n", item, itemType);
	}
}
