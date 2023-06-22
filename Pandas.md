# Pandas

## Pandas 개요

### 개요

- 파이썬에서 데이터 조작과 분석을 위한 라이브러리
- 수치 테이블과 시계열을 처리하는 데이터 구조와 연산 방법을 제공
- 판다스로 처리하기 좋은 데이터
    - SQL 테이블이나 엑셀처럼 여러 형식을 갖는 테이블형 데이터
    - 순서에 따라 정렬되거나 정렬되지 않은 시계열 데이터
    - 행과 열 라벨이 있는 임의의 행렬 데이터
    - 관측 / 통계 데이터 시트

### Pandas 데이터 구조

![Untitled](Pandas%20860c0d91ad2444cba8ad3f228bb59e08/Untitled.png)

- **DataFrame**
    - 2차원 데이터 구조로, 행과 열로 구성된 테이블 형태의 데이터
- **Index**
    - 데이터 구조에서 각 항목을 식별하는 레이블
    - 데이터에 대한 고유한 식별자 역할
- **Series**
    - 1차원 데이터 배열을 나타내는 객체
    - 단일 열을 가지고 있으며, 행 이름(index)과 열의 값(value)으로 구성
    - 데이터를 라벨링하고 인덱싱하여 데이터에 쉽게 접근할 수 있

### 라이브러리

```python
import pandas as pd
```

### 관련 함수

```python
#print(dir(pd))

'''
['ArrowDtype', 'BooleanDtype', 'Categorical', 'CategoricalDtype', 
'CategoricalIndex', 'DataFrame', 'DateOffset', 'DatetimeIndex', 
'DatetimeTZDtype', 'ExcelFile', 'ExcelWriter', 'Flags', 'Float32Dtype', 
'Float64Dtype', 'Grouper', 'HDFStore', 'Index', 'IndexSlice', 
'Int16Dtype', 'Int32Dtype', 'Int64Dtype', 'Int8Dtype', 'Interval', 
'IntervalDtype', 'IntervalIndex', 'MultiIndex', 'NA', 'NaT', 
'NamedAgg', 'Period', 'PeriodDtype', 'PeriodIndex', 'RangeIndex', 
'Series', 'SparseDtype', 'StringDtype', 'Timedelta', 'TimedeltaIndex', 
'Timestamp', 'UInt16Dtype', 'UInt32Dtype', 'UInt64Dtype', 
'UInt8Dtype', '__all__', '__builtins__', '__cached__', '__doc__', 
'__docformat__', '__file__', '__git_version__', '__loader__', 
'__name__', '__package__', '__path__', '__spec__', '__version__', 
'_config', '_is_numpy_dev', '_libs', '_testing', '_typing', '_version', 
'annotations', 'api', 'array', 'arrays', 'bdate_range', 'compat', 
'concat', 'core', 'crosstab', 'cut', 'date_range', 'describe_option', 
'errors', 'eval', 'factorize', 'from_dummies', 'get_dummies', 
'get_option', 'infer_freq', 'interval_range', 'io', 'isna', 'isnull', 
'json_normalize', 'lreshape', 'melt', 'merge', 'merge_asof', 
'merge_ordered', 'notna', 'notnull', 'offsets', 'option_context', 
'options', 'pandas', 'period_range', 'pivot', 'pivot_table', 
'plotting', 'qcut', 'read_clipboard', 'read_csv', 'read_excel', 
'read_feather', 'read_fwf', 'read_gbq', 'read_hdf', 'read_html', 
'read_json', 'read_orc', 'read_parquet', 'read_pickle', 'read_sas', 
'read_spss', 'read_sql', 'read_sql_query', 'read_sql_table', 
'read_stata', 'read_table', 'read_xml', 'reset_option', 
'set_eng_float_format', 'set_option', 'show_versions', 'test', 
'testing', 'timedelta_range', 'to_datetime', 'to_numeric', 
'to_pickle', 'to_timedelta', 'tseries', 'unique', 'util', 
'value_counts', 'wide_to_long']

'''
```

```python
# print(dir(df))

'''
['T', '_AXIS_LEN', '_AXIS_ORDERS', '_AXIS_TO_AXIS_NUMBER', 
'_HANDLED_TYPES', '__abs__', '__add__', '__and__', '__annotations__', 
'__array__', '__array_priority__', '__array_ufunc__', '__bool__', 
'__class__', '__contains__', '__copy__', '__dataframe__', 
'__deepcopy__', '__delattr__', '__delitem__', '__dict__', '__dir__', 
'__divmod__', '__doc__', '__eq__', '__finalize__', '__floordiv__', 
'__format__', '__ge__', '__getattr__', '__getattribute__', 
'__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', 
'__iand__', '__ifloordiv__', '__imod__', '__imul__', '__init__', 
'__init_subclass__', '__invert__', '__ior__', '__ipow__', '__isub__', 
'__iter__', '__itruediv__', '__ixor__', '__le__', '__len__', '__lt__', 
'__matmul__', '__mod__', '__module__', '__mul__', '__ne__', '__neg__', 
'__new__', '__nonzero__', '__or__', '__pos__', '__pow__', '__radd__', 
'__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', 
'__rfloordiv__', '__rmatmul__', '__rmod__', '__rmul__', '__ror__', 
'__round__', '__rpow__', '__rsub__', '__rtruediv__', '__rxor__', 
'__setattr__', '__setitem__', '__setstate__', '__sizeof__', '__str__', 
'__sub__', '__subclasshook__', '__truediv__', '__weakref__', 
'__xor__', '_accessors', '_accum_func', '_add_numeric_operations', 
'_agg_examples_doc', '_agg_summary_and_see_also_doc', '_align_frame', 
'_align_series', '_append', '_arith_method', '_as_manager', '_attrs', 
'_box_col_values', '_can_fast_transpose', 
'_check_inplace_and_allows_duplicate_labels', 
'_check_inplace_setting', '_check_is_chained_assignment_possible', 
'_check_label_or_level_ambiguity', '_check_setitem_copy', 
'_clear_item_cache', '_clip_with_one_bound', '_clip_with_scalar', 
'_cmp_method', '_combine_frame', '_consolidate', 
'_consolidate_inplace', '_construct_axes_dict', '_construct_result', 
'_constructor', '_constructor_sliced', 
'_create_data_for_split_and_tight_to_dict', '_data', 
'_dir_additions', '_dir_deletions', '_dispatch_frame_op', 
'_drop_axis', '_drop_labels_or_levels', '_ensure_valid_index', 
'_find_valid_index', '_flags', '_from_arrays', '_get_agg_axis', 
'_get_axis', '_get_axis_name', '_get_axis_number', 
'_get_axis_resolvers', '_get_block_manager_axis', '_get_bool_data', 
'_get_cleaned_column_resolvers', '_get_column_array', 
'_get_index_resolvers', '_get_item_cache', '_get_label_or_level_values', 
'_get_numeric_data', '_get_value', '_getitem_bool_array', 
'_getitem_multilevel', '_getitem_nocopy', '_gotitem', 
'_hidden_attrs', '_indexed_same', '_info_axis', '_info_axis_name', 
'_info_axis_number', '_info_repr', '_init_mgr', '_inplace_method', 
'_internal_names', '_internal_names_set', '_is_copy', 
'_is_homogeneous_type', '_is_label_or_level_reference', 
'_is_label_reference', '_is_level_reference', '_is_mixed_type', 
'_is_view', '_iset_item', '_iset_item_mgr', '_iset_not_inplace', 
'_item_cache', '_iter_column_arrays', '_ixs', '_join_compat', 
'_logical_func', '_logical_method', '_maybe_cache_changed', 
'_maybe_update_cacher', '_metadata', '_mgr', 
'_min_count_stat_function', '_needs_reindex_multi', 
'_protect_consolidate', '_reduce', '_reduce_axis1', '_reindex_axes', 
'_reindex_columns', '_reindex_index', '_reindex_multi', 
'_reindex_with_indexers', '_rename', '_replace_columnwise', 
'_repr_data_resource_', '_repr_fits_horizontal_', 
'_repr_fits_vertical_', '_repr_html_', '_repr_latex_', '_reset_cache', 
'_reset_cacher', '_sanitize_column', '_series', '_set_axis', 
'_set_axis_name', '_set_axis_nocheck', '_set_is_copy', '_set_item', 
'_set_item_frame_value', '_set_item_mgr', '_set_value', 
'_setitem_array', '_setitem_frame', '_setitem_slice', '_slice', 
'_stat_axis', '_stat_axis_name', '_stat_axis_number', '_stat_function', 
'_stat_function_ddof', '_take', '_take_with_is_copy', 
'_to_dict_of_blocks', '_to_latex_via_styler', '_typ', 
'_update_inplace', '_validate_dtype', '_values', '_where', 'abs', 
'add', 'add_prefix', 'add_suffix', 'agg', 'aggregate', 'align', 
'all', 'any', 'apply', 'applymap', 'asfreq', 'asof', 'assign', 
'astype', 'at', 'at_time', 'attrs', 'axes', 'backfill', 'between_time', 
'bfill', 'bool', 'boxplot', 'clip', 'col1', 'col2', 'col3', 
'columns', 'combine', 'combine_first', 'compare', 'convert_dtypes', 
'copy', 'corr', 'corrwith', 'count', 'cov', 'cummax', 'cummin', 
'cumprod', 'cumsum', 'describe', 'diff', 'div', 'divide', 'dot', 
'drop', 'drop_duplicates', 'droplevel', 'dropna', 'dtypes', 
'duplicated', 'empty', 'eq', 'equals', 'eval', 'ewm', 'expanding', 
'explode', 'ffill', 'fillna', 'filter', 'first', 'first_valid_index', 
'flags', 'floordiv', 'from_dict', 'from_records', 'ge', 'get', 
'groupby', 'gt', 'head', 'hist', 'iat', 'idxmax', 'idxmin', 'iloc', 
'index', 'infer_objects', 'info', 'insert', 'interpolate', 'isetitem', 
'isin', 'isna', 'isnull', 'items', 'iterrows', 'itertuples', 'join', 
'keys', 'kurt', 'kurtosis', 'last', 'last_valid_index', 'le', 'loc', 
'lt', 'mask', 'max', 'mean', 'median', 'melt', 'memory_usage', 
'merge', 'min', 'mod', 'mode', 'mul', 'multiply', 'ndim', 'ne', 
'nlargest', 'notna', 'notnull', 'nsmallest', 'nunique', 'pad', 
'pct_change', 'pipe', 'pivot', 'pivot_table', 'plot', 'pop', 'pow', 
'prod', 'product', 'quantile', 'query', 'radd', 'rank', 'rdiv', 
'reindex', 'reindex_like', 'rename', 'rename_axis', 'reorder_levels', 
'replace', 'resample', 'reset_index', 'rfloordiv', 'rmod', 'rmul', 
'rolling', 'round', 'rpow', 'rsub', 'rtruediv', 'sample', 
'select_dtypes', 'sem', 'set_axis', 'set_flags', 'set_index', 'shape', 
'shift', 'size', 'skew', 'sort_index', 'sort_values', 'squeeze', 
'stack', 'std', 'style', 'sub', 'subtract', 'sum', 'swapaxes', 
'swaplevel', 'tail', 'take', 'to_clipboard', 'to_csv', 'to_dict', 
'to_excel', 'to_feather', 'to_gbq', 'to_hdf', 'to_html', 'to_json', 
'to_latex', 'to_markdown', 'to_numpy', 'to_orc', 'to_parquet', 
'to_period', 'to_pickle', 'to_records', 'to_sql', 'to_stata', 
'to_string', 'to_timestamp', 'to_xarray', 'to_xml', 'transform', 
'transpose', 'truediv', 'truncate', 'tz_convert', 'tz_localize', 
'unstack', 'update', 'value_counts', 'values', 'var', 'where', 'xs']
'''
```

```python
# Series 요소
#print(dir(name))
'''
['T', '_AXIS_LEN', '_AXIS_ORDERS', '_AXIS_TO_AXIS_NUMBER', 
'_HANDLED_TYPES', '__abs__', '__add__', '__and__', '__annotations__', 
'__array__', '__array_priority__', '__array_ufunc__', '__bool__', 
'__class__', '__contains__', '__copy__', '__deepcopy__', 
'__delattr__', '__delitem__', '__dict__', '__dir__', '__divmod__', 
'__doc__', '__eq__', '__finalize__', '__float__', '__floordiv__', 
'__format__', '__ge__', '__getattr__', '__getattribute__', 
'__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', 
'__iand__', '__ifloordiv__', '__imod__', '__imul__', '__init__', 
'__init_subclass__', '__int__', '__invert__', '__ior__', '__ipow__', 
'__isub__', '__iter__', '__itruediv__', '__ixor__', '__le__', 
'__len__', '__lt__', '__matmul__', '__mod__', '__module__', 
'__mul__', '__ne__', '__neg__', '__new__', '__nonzero__', '__or__', 
'__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', 
'__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', 
'__rmatmul__', '__rmod__', '__rmul__', '__ror__', '__round__', 
'__rpow__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', 
'__setitem__', '__setstate__', '__sizeof__', '__str__', '__sub__', 
'__subclasshook__', '__truediv__', '__weakref__', '__xor__', 
'_accessors', '_accum_func', '_add_numeric_operations', 
'_agg_examples_doc', '_agg_see_also_doc', '_align_frame', 
'_align_series', '_append', '_arith_method', '_as_manager', 
'_attrs', '_binop', '_can_hold_na', 
'_check_inplace_and_allows_duplicate_labels', '_check_inplace_setting', 
'_check_is_chained_assignment_possible', '_check_label_or_level_ambiguity', 
'_check_setitem_copy', '_clear_item_cache', 
'_clip_with_one_bound', '_clip_with_scalar', '_cmp_method', 
'_consolidate', '_consolidate_inplace', '_construct_axes_dict', 
'_construct_result', '_constructor', '_constructor_expanddim', 
'_convert_dtypes', '_data', '_dir_additions', '_dir_deletions', 
'_drop_axis', '_drop_labels_or_levels', '_duplicated', 
'_find_valid_index', '_flags', '_get_axis', '_get_axis_name', 
'_get_axis_number', '_get_axis_resolvers', '_get_block_manager_axis', 
'_get_bool_data', '_get_cacher', '_get_cleaned_column_resolvers', 
'_get_index_resolvers', '_get_label_or_level_values', 
'_get_numeric_data', '_get_value', '_get_values', '_get_values_tuple', 
'_get_with', '_gotitem', '_hidden_attrs', '_indexed_same', 
'_info_axis', '_info_axis_name', '_info_axis_number', '_init_dict', 
'_init_mgr', '_inplace_method', '_internal_names', 
'_internal_names_set', '_is_cached', '_is_copy', 
'_is_label_or_level_reference', '_is_label_reference', 
'_is_level_reference', '_is_mixed_type', '_is_view', '_item_cache', 
'_ixs', '_logical_func', '_logical_method', '_map_values', 
'_maybe_update_cacher', '_memory_usage', '_metadata', '_mgr', 
'_min_count_stat_function', '_name', '_needs_reindex_multi', 
'_protect_consolidate', '_reduce', '_references', '_reindex_axes', 
'_reindex_indexer', '_reindex_multi', '_reindex_with_indexers', 
'_rename', '_replace_single', '_repr_data_resource_', '_repr_latex_', 
'_reset_cache', '_reset_cacher', '_set_as_cached', '_set_axis', 
'_set_axis_name', '_set_axis_nocheck', '_set_is_copy', '_set_labels', 
'_set_name', '_set_value', '_set_values', '_set_with', 
'_set_with_engine', '_slice', '_stat_axis', '_stat_axis_name', 
'_stat_axis_number', '_stat_function', '_stat_function_ddof', '_take', 
'_take_with_is_copy', '_to_latex_via_styler', '_typ', '_update_inplace', 
'_validate_dtype', '_values', '_where', 'abs', 'add', 'add_prefix', 
'add_suffix', 'agg', 'aggregate', 'align', 'all', 'any', 'apply', 
'argmax', 'argmin', 'argsort', 'array', 'asfreq', 'asof', 'astype', 
'at', 'at_time', 'attrs', 'autocorr', 'axes', 'backfill', 'between', 
'between_time', 'bfill', 'bool', 'clip', 'combine', 'combine_first', 
'compare', 'convert_dtypes', 'copy', 'corr', 'count', 'cov', 'cummax', 
'cummin', 'cumprod', 'cumsum', 'describe', 'diff', 'div', 'divide', 
'divmod', 'dot', 'drop', 'drop_duplicates', 'droplevel', 'dropna', 
'dtype', 'dtypes', 'duplicated', 'empty', 'eq', 'equals', 'ewm', 
'expanding', 'explode', 'factorize', 'ffill', 'fillna', 'filter', 
'first', 'first_valid_index', 'flags', 'floordiv', 'ge', 'get', 
'groupby', 'gt', 'hasnans', 'head', 'hist', 'iat', 'idxmax', 'idxmin', 
'iloc', 'index', 'infer_objects', 'info', 'interpolate', 
'is_monotonic_decreasing', 'is_monotonic_increasing', 'is_unique', 
'isin', 'isna', 'isnull', 'item', 'items', 'keys', 'kurt', 'kurtosis', 
'last', 'last_valid_index', 'le', 'loc', 'lt', 'map', 'mask', 'max', 
'mean', 'median', 'memory_usage', 'min', 'mod', 'mode', 'mul', 
'multiply', 'name', 'nbytes', 'ndim', 'ne', 'nlargest', 'notna', 
'notnull', 'nsmallest', 'nunique', 'pad', 'pct_change', 'pipe', 
'plot', 'pop', 'pow', 'prod', 'product', 'quantile', 'radd', 'rank', 
'ravel', 'rdiv', 'rdivmod', 'reindex', 'reindex_like', 'rename', 
'rename_axis', 'reorder_levels', 'repeat', 'replace', 'resample', 
'reset_index', 'rfloordiv', 'rmod', 'rmul', 'rolling', 'round', 
'rpow', 'rsub', 'rtruediv', 'sample', 'searchsorted', 'sem', 
'set_axis', 'set_flags', 'shape', 'shift', 'size', 'skew', 'sort_index', 
'sort_values', 'squeeze', 'std', 'str', 'sub', 'subtract', 'sum', 
'swapaxes', 'swaplevel', 'tail', 'take', 'to_clipboard', 'to_csv', 
'to_dict', 'to_excel', 'to_frame', 'to_hdf', 'to_json', 'to_latex', 
'to_list', 'to_markdown', 'to_numpy', 'to_period', 'to_pickle', 
'to_sql', 'to_string', 'to_timestamp', 'to_xarray', 'transform', 
'transpose', 'truediv', 'truncate', 'tz_convert', 'tz_localize', 
'unique', 'unstack', 'update', 'value_counts', 'values', 'var', 
'view', 'where', 'xs']
```

## DataFrame

### DataFrame 생성

> **DataFrame 생성 방법**

**1) Dict 이용**
   df = pd.DataFrame(dict)

**2) 중첩 리스트 이용**
   df = pd.DataFrame(중첩리스트, index=[ ], columns=[ ]

**3) np.Series(리스트) 이용**
   - df = pd.DataFrame( [ Series, Series, … ] )
   - (하나의) Series는 DataFrame으로 변경 가능
     df = Series.to_frame(이름)
> 

- **dict 이용**
    
    ```python
    print("1. dict 이용한 DataFrame 생성")
    df = pd.DataFrame({"col1" : [4 ,5, 6],
                       "col2" : [7, 8, 9],
                       "col3" : [10, 11, 12]})
    print(df)
    '''
       col1  col2  col3
    0     4     7    10
    1     5     8    11
    2     6     9    12
    '''
    
    print(df, type(df)) # <class 'pandas.core.frame.DataFrame'>
    '''
       col1  col2  col3
    0     4     7    10
    1     5     8    11
    2     6     9    12
    '''
    ```
    
- **중첩 리스트 이용한 DataFrame 생성 ⇒ ndarray도 가능**
    
    ```python
    df = pd.DataFrame([[4, 7, 10],[5, 8, 11],[6, 9, 12]],
                      index=[1, 2, 3], 
                      columns=['col1', 'col2', 'col3']) 
    # default index 0,1,2를 1,2,3으로 바꿔줌
    # default 0,1,2에 컬럼명 지정
    
    print(df, type(df)) # <class 'pandas.core.frame.DataFrame'>
    '''
       col1  col2  col3
    1     4     7    10
    2     5     8    11
    3     6     9    12
    '''
    ```
    
- **DataFrame 생성 - Series 사용**
    
    ```python
    name = pd.Series(["유관순","안중근"])
    age = pd.Series([18,31])
    birthday = pd.Series(['1920/09/28','1910/03/26'])
    
    hero = pd.DataFrame([name,age,birthday])
    hero.columns =["hero1", "hero2"]
    hero.index =["이름","나이","생일"]
    print(hero) # Series는 기본적으로 행단위 데이터프레임으로 만든다.
    '''
    							hero1       hero2
    이름         유관순         안중근
    나이          18          31
    생일  1920/09/28  1910/03/26
    '''
    print(hero.T)
    '''
    				이름  나이    생일
    hero1  유관순  18  1920/09/28
    hero2  안중근  31  1910/03/26
    '''
    ```
    

### DataFrame 속성 정보 보기

> **1) 컬럼 정보**
  df.columns 또는 df.key( )

**2) 인덱스(라벨) 정보**
  df.index

**3) 값 정보**
  df.value 또는 df.to_numpy( ) - 권장
> 

- **컬럼 정보 보기 ⇒ 리스트로 반**
    
    ```python
    # 원본 데이터
    
    df = pd.DataFrame({"col1" : [4 ,5, 6],
                       "col2" : [7, 8, 9],
                       "col3" : [10, 11, 12]},index=['A','B','C'])
    print(df)
    '''
    col1  col2  col3
    A     4     7    10
    B     5     8    11
    C     6     9    12
    '''
    ```
    
    ```python
    print(df.columns)
    # Index(['col1', 'col2', 'col3'], dtype='object')
    
    print(df.keys())
    # Index(['col1', 'col2', 'col3'], dtype='object')
    ```
    
- **인덱스(라벨) 정보 보기 ⇒ 리스트로 반환**
    
    ```python
    print(df.index)
    # Index(['A', 'B', 'C'], dtype='object')
    ```
    
- **값(value) 정보 보기 ⇒ 다차원 배열로 반환**
    
    ```python
    print(df.values)
    print(df.to_numpy())
    '''
    [[ 4  7 10]
     [ 5  8 11]
     [ 6  9 12]]
    '''
    ```
    

## 인덱스 및 컬럼명 변경

### 컬럼명 변경

```python
# 원본 데이터

df = pd.DataFrame({"col1" : [4 ,5, 6],
                   "col2" : [7, 8, 9],
                   "col3" : [10, 11, 12]})
print(df)
'''
		col1  col2  col3
0     4     7    10
1     5     8    11
2     6     9    12
'''
```

```python
df.columns=['c1','c2','c3']
print(df)
'''
	c1  c2  c3
0   4   7  10
1   5   8  11
2   6   9  12
'''
```

### 인덱스(라벨)명 변경

- **pd.DataFrame( ..., index=[값, 값2,...] )**
    
    ```python
    df = pd.DataFrame({"col1" : [4 ,5, 6],
                       "col2" : [7, 8, 9],
                       "col3" : [10, 11, 12]}, index=['A','B','C'])
    print(df)
    '''
    		col1  col2  col3
    A     4     7    10
    B     5     8    11
    C     6     9    12
    '''
    ```
    
- **df.index =[ 값, 값2, ... ]**
    
    ```python
    df.index=[10,20,30]
    print(df)
    '''
    		col1  col2  col3
    10     4     7    10
    20     5     8    11
    30     6     9    12
    '''
    ```
    

## 인덱스 관리

### 기존 컬럼을 인덱스로 변경 (df.set_index)

```python
# 원본 데이터

df = pd.DataFrame({    "date":['2021','2022'],
                       "City": ["Seoul", "Seoul"],
                       "Temperature": [32, 34]
                       })

print(df)
'''
	date   City    Temperature
0  2021  Seoul           32
1  2022  Seoul           34
'''
```

```python
df.set_index('date', inplace=True)

print(df)
'''
			City     Temperature
date                    
2021  Seoul           32
2022  Seoul           34
'''

print(df.index)
# Index(['2021', '2022'], dtype='object', name='date')
```

### 기존 인덱스를 컬럼으로 변경하고 새로운 인덱스 생성 (df.reset_index)

- **기존 인덱스는 컬럼으로 변경하고 새로운 인덱스 생성**
    
    ```python
    # 원본 데이터
    '''
    			City     Temperature
    date                    
    2021  Seoul           32
    2022  Seoul           34
    '''
    
    df.reset_index(inplace=True, drop=False)  
    # 기존 인덱스(date)를 컬럼으로 변경하고 새로운 인덱스(0,1) 생성
    
    print(df)
    '''
       date   City  Temperature
    0  2021  Seoul           32
    1  2022  Seoul           34
    '''
    ```
    
- **기존 인덱스(date)는 삭하고 새로운 인덱스 생성**
    
    ```python
    # 원본 데이터
    '''
    			City     Temperature
    date                    
    2021  Seoul           32
    2022  Seoul           34
    '''
    
    df.reset_index(inplace=True, drop=True)     
    # 기존 인덱스를 삭제하고 새로운 인덱스 생성
    
    print(df)
    '''
        City  Temperature
    0  Seoul           32
    1  Seoul           34
    '''
    ```
    

### 기존 인덱스 재배치 (reindex)

```python
# 원본 데이터

df = pd.DataFrame({ "date":['2021','2022','2012','2023','2024'],
                    "City": ["Seoul", "Seoul", "Seoul","Seoul","Seoul"],
                    "Temperature": [32, 34,32, 34,53]
                  },index=list('AECBD'))

print(df)
'''
   date   City  Temperature
A  2021  Seoul           32
E  2022  Seoul           34
C  2012  Seoul           32
B  2023  Seoul           34
D  2024  Seoul           53
'''
```

```python
new_df = df.reindex(index=list('ABCDE')) 
# 원하는 리스트 지정해서 리스트 재배치

print(new_df)
'''
   date   City  Temperature
A  2021  Seoul           32
B  2023  Seoul           34
C  2012  Seoul           32
D  2024  Seoul           53
E  2022  Seoul           34
'''
```

### 중복되는 인덱스 방지 (ignore_index)

<aside>
💡 DataFrame 병합 시 기존 index 중복 발생
⇒ ignore_index=True로 index를 재설정

</aside>

```python
df1 = pd.DataFrame({'a':[12,2]},
                   index=[1,2])
df2 = pd.DataFrame({'a':[120,20]},
                   index=[1,2])

new_df = pd.concat([df1, df2])
print(new_df)
'''
     a
1   12
2    2
1  120
2   20
'''
```

```python
new_df = pd.concat([df1, df2], ignore_index=True)
print(new_df)
'''
     a
0   12
1    2
2  120
3   20
'''
```

<aside>
💡 자동으로 새 인덱스를 생성하여 병합

</aside>

## 색인

### 컬럼 색인

- **싱글 컬럼 조회**
    
    ```python
    # 원본 데이터
    
    df = pd.DataFrame({"col1" : [4 ,5, 6, 6],
                       "col2" : [7, 8, 9, 9],
                       "col3" : [10, 11, 12, 12]},
                       index = list("ABCD"))
    print(df)
    '''
    		col1  col2  col3
    A     4     7    10
    B     5     8    11
    C     6     9    12
    D     6     9    12
    '''
    ```
    
    ```python
    print(df.col1 )     # Series 반환
    print(df['col1'])   # Series 반환
    
    '''
    A    4
    B    5
    C    6
    D    6
    Name: col1, dtype: int64 <- 이런 형태 = Series
    '''
    ```
    
    <aside>
    💡 싱글 컬럼 조회시 Series로 반환됨
    
    </aside>
    
- **멀티 컬럼 조회**
    
    ```python
    print(df[['col2', 'col1']])
    '''
    col2  col1
    A     7     4
    B     8     5
    C     9     6
    D     9     6
    '''
    ```
    
- **특정 컬럼만 여러번 조회**
    
    ```python
    print(df[['col1','col1','col1']])
    '''
    col1  col1  col1
    A     4     4     4
    B     5     5     5
    C     6     6     6
    D     6     6     6
    '''
    ```
    

### 행(라벨) 색인

- **행 인덱스의 label 이용 ( df.loc )**
    1. **단일 행 조회**
        
        ```python
        # 원본 데이터
        
        df = pd.DataFrame({"col1" : [4 ,5, 6, 6,1],
                           "col2" : [7, 8, 9, 9,2],
                           "col3" : [10, 11, 12, 12,10]},
                           index = list("ABCDE"))
        print(df)
        '''
            col1  col2  col3
        A     4     7    10
        B     5     8    11
        C     6     9    12
        D     6     9    12
        E     1     2    10
        '''
        ```
        
        ```python
        print(df.loc["A"]) # Series 반환
        '''
        col1     4
        col2     7
        col3    10
        Name: A, dtype: int64
        '''
        ```
        
        <aside>
        💡 단일 행 조회 시 Series로 반환됨
        
        </aside>
        
    
    1. **멀티 행 조회**
        1. **fancy label**
            
            ```python
            # A 와 B행 출력
            
            print(df.loc[["A","B"]])
            '''
            col1  col2  col3
            A     4     7    10
            B     5     8    11
            '''
            ```
            
        2. **slicing label**
            
            ```python
            # B행부터 D행까지 출력
            
            print(df.loc["B":"D"])
            '''
            col1  col2  col3
            B     5     8    11
            C     6     9    12
            D     6     9    12
            '''
            ```
            
        3. **boolean label**
            
            ```python
            # A,C,E행 출력
            
            print(df.loc[[True,False,True,False,True]])
            '''
            col1  col2  col3
            A     4     7    10
            C     6     9    12
            E     1     2    10
            '''
            ```
            
- **행 위치 이용 ( df.iloc )**
    1. **단일 행 조회**
        
        ```python
        # 원본 데이터
        
        df = pd.DataFrame({"col1" : [4 ,5, 6, 6,1],
                           "col2" : [7, 8, 9, 9,2],
                           "col3" : [10, 11, 12, 12,10]},
                           index = list("ABCDE"))
        print(df)
        '''
                  col1  col2  col3
        0     A     4     7    10
        1     B     5     8    11
        2     C     6     9    12
        3     D     6     9    12
        4     E     1     2    10
        '''
        ```
        
        ```python
        # A 행 출력
        print(df.iloc[0]) # Series 반환
        '''
        col1     4
        col2     7
        col3    10
        Name: A, dtype: int64
        '''
        ```
        
    2. **멀티 행 조회**
        1. **fancy 위치**
            
            ```python
            # A 와 B행 출력
            print(df.iloc[[0,1]]) # DataFrame 반환
            
            '''
            col1  col2  col3
            A     4     7    10
            B     5     8    11
            '''
            ```
            
        2. **slicing 위치**
            
            ```python
            # B행부터 D행까지 출력
            print(df.iloc[1:-1]) # DataFrame 반환
            '''
            col1  col2  col3
            B     5     8    11
            C     6     9    12
            D     6     9    12
            '''
            ```
            
        3. **boolean 위치**
            
            ```python
            # A,C,E행 출력
            print(df.iloc[[True,False,True,False,True]]) # DataFrame 반환
            '''
            col1  col2  col3
            A     4     7    10
            C     6     9    12
            E     1     2    10
            '''
            ```
            

### 행 및 컬럼 색인

- **행 인덱스의 label 이용**
    
    > ⇒ 기본 문법 df.loc[ 행 label, 컬럼 label ]
    ⇒ 행 label은 인덱스 라벨, fancy, 슬라이싱, boolean 모두 가능
    ⇒ 컬럼 label은 인덱스 라벨, fancy, 슬라이싱, boolean 모두 가능
    > 
    
    ```python
    # 원본 데이터
    
    df = pd.DataFrame({"col1": [4, 5, 6, 6, 1],
                       "col2": [7, 8, 9, 9, 2],
                       "col3": [10, 11, 12, 12, 10]},
                      index=list("ABCDE"))
    
    print(df)
    '''
       col1  col2  col3
    A     4     7    10
    B     5     8    11
    C     6     9    12
    D     6     9    12
    E     1     2    10
    '''
    ```
    
    1. **인덱싱**
        
        ```python
        # A행, col1만 조회
        
        print(df.loc['A','col1'])
        # 4
        ```
        
        <aside>
        💡 하나의 행+하나의 컬럼 조회 시 스칼라값으로 반환
        
        </aside>
        
    2. **인덱싱 + fancy**
        
        ```python
        # A, B행 + col1 컬럼 조회
        
        print(df.loc[['A','B'],'col1']) # Series 반환
        '''
        A    4
        B    5
        Name: col1, dtype: int64
        '''
        ```
        
        <aside>
        💡 컬럼 하나만 조회 시 Series로 반환
        
        </aside>
        
    3. **fancy + fancy**
        
        ```python
        # A, B행 + col1, col2 컬럼 조회
        
        print(df.loc[['A','B'],['col1','col2']]) # DataFrame 반환
        '''
           col1  col2
        A     4     7
        B     5     8
        '''
        ```
        
    4. **slice + fancy**
        
        ```python
        print(df.loc['B':'E',['col1','col2']]) # DataFrame 반환
        '''
           col1  col2
        B     5     8
        C     6     9
        D     6     9
        E     1     2
        '''
        ```
        
    5. **slice + slice**
        
        ```python
        print(df.loc['B':'E','col1':'col3']) # DataFrame 반환
        '''
           col1  col2  col3
        B     5     8    11
        C     6     9    12
        D     6     9    12
        E     1     2    10
        '''
        ```
        
    6. **boolean + slice**
        
        ```python
        print(df.loc[[True,False,True,False,True],'col2':'col3']) # DataFrame 반환
        '''
           col2  col3
        A     7    10
        C     9    12
        E     2    10
        '''
        ```
        
- **행 인덱스의 위치 이용**
    
    > ⇒ 기본 문법 df.iloc[ 행 위치, 컬럼 위치 ]
    > 
    
    ```python
    # 원본 데이터
    
    df = pd.DataFrame({"col1": [4, 5, 6, 6, 1],
                       "col2": [7, 8, 9, 9, 2],
                       "col3": [10, 11, 12, 12, 10]},
                      index=list("ABCDE"))
    
    print(df)
    '''
              0      1    2
             col1  col2  col3
    0    A     4     7    10
    1    B     5     8    11
    2    C     6     9    12
    3    D     6     9    12
    4    E     1     2    10
    '''
    ```
    
    1. **인덱싱**
        
        ```python
        print(df.iloc[0,0]) # 4 (스칼라값)
        ```
        
    2. **인덱싱 + fancy**
        
        ```python
        print(df.iloc[[0,1],0]) # Series 반환
        '''
        A    4
        B    5
        Name: col1, dtype: int64
        '''
        ```
        
    3. **fancy + fancy**
        
        ```python
        print(df.iloc[[0,1],[0,1]]) # DataFrame 반환
        '''
           col1  col2
        A     4     7
        B     5     8
        '''
        ```
        
    4. **slice + fancy**
        
        ```python
        print(df.iloc[1:,[0,1]]) # DataFrame 반환
        '''
           col1  col2
        B     5     8
        C     6     9
        D     6     9
        E     1     2
        '''
        ```
        
    5. **slice + slice** 
        
        ```python
        print(df.iloc[1:, 0:]) # DataFrame 반환
        '''
           col1  col2  col3
        B     5     8    11
        C     6     9    12
        D     6     9    12
        E     1     2    10
        '''
        ```
        
    6. **boolean+ slice** 
        
        ```python
        print(df.iloc[[True,False,True,False,True],1:]) # DataFrame 반환
        '''
           col2  col3
        A     7    10
        C     9    12
        E     2    10
        '''
        ```
        

### 값 변경

```python
# 원본 데이터

df = pd.DataFrame({"col1": [4, 5, 6, 6, 1],
                   "col2": [7, 8, 9, 9, 2],
                   "col3": [10, 11, 12, 12, 10]},
                  index=list("ABCDE"))

print(df)
'''
          0      1    2
         col1  col2  col3
0    A     4     7    10
1    B     5     8    11
2    C     6     9    12
3    D     6     9    12
4    E     1     2    10
'''
```

- **df.loc[행, 열]**
    - D행의 col2 값 변경
        
        ```python
        df.loc['D','col2'] = 900
        #df.iloc[3,1] = 900
        print(df)
        '''
           col1  col2  col3
        A   100   100   100
        B   200   200   200
        C   200   200   200
        D     6   900    12
        E     1     2    10
        '''
        ```
        
- **인덱싱**
    - A행의 모든 값 변경
        
        ```python
        df.loc['A'] = 100
        print(df)
        '''
           col1  col2  col3
        A   100   100   100
        B     5     8    11
        C     6     9    12
        D     6     9    12
        E     1     2    10
        '''
        ```
        
- **fancy**
    - B행, C행의 모든 값 변경
        
        ```python
        df.loc[['B','C']] = 200
        print(df)
        '''
           col1  col2  col3
        A   100   100   100
        B   200   200   200
        C   200   200   200
        D     6     9    12
        E     1     2    10
        '''
        ```
        
    - D행, E행의 col1, col3 값 변경
        
        ```python
        df.loc[['D','E'],['col1','col3']]=-1
        print(df)
        '''
        col1  col2  col3
        A   100   100   100
        B   200   200   200
        C   200   200   200
        D    -1   900    -1
        E    -1     2    -1
        '''
        ```
        
    - **slice**
        - A행~D행의 col3 값 변경
            
            ```python
            #df.loc[['D','E'],['col1','col3']]=-1
            df.loc['A':'D','col3']=-100
            print(df)
            '''
            col1  col2  col3
            A   100   100  -100
            B   200   200  -100
            C   200   200  -100
            D    -1   900  -100
            E    -1     2    -1
            '''
            ```
            
    - **boolean**
        - E행 col2의 값 변경
            
            ```python
            df.loc['E',[False,True,False]]=200
            print(df)
            '''
            col1  col2  col3
            A   100   100  -100
            B   200   200  -100
            C   200   200  -100
            D    -1   900  -100
            E    -1   200    -1
            '''
            ```
            

## 컬럼 추가(마지막 열에)

### df['컬럼명'] = 리스트 | series

- **df['컬럼명'] = 리스트**
    
    ```python
    # 원본 데이
    
    df = pd.DataFrame({"이름":['홍길동','이순신','유관순','강감찬'],
                       "국어":[30, 26, 11, 10],
                       "수학":[20, 12, 20, 12]
                     }, index=[1,2,3,4])
    # 1. DataFrame 생성
    print("1. DataFrame")
    print(df)
    '''
        이름  국어  수학
    1  홍길동  30  20
    2  이순신  26  12
    3  유관순  11  20
    4  강감찬  10  12
    '''
    ```
    
    ```python
    # 영어 컬럼 추가
    
    df['영어']=[10,20,30,40]
    print(df)
    '''
    	이름  국어  수학  영어
    1  홍길동  30  20  10
    2  이순신  26  12  20
    3  유관순  11  20  30
    4  강감찬  10  12  40
    '''
    ```
    
    ```python
    # 총합 컬럼 추가
    df['총합']= df['영어'] + df['국어'] + df['수학'] + df['과학']
    ```
    
    <aside>
    💡 DataFrame끼리도 연산 가능하다.
    
    </aside>
    
    ```python
    # 평균 컬럼 추가
    df['평균']= np.round(df['총합']/4,1)
    
    # => 결과 값이 실수로 출력된다. 정수로 바꾸고 싶을 때
    df['평균']= df['평균'].astype(np.int32)
    ```
    
    ```python
    # 3항 연산자 사용
    # 평균이 20보다 크면 '합격 작으면 '불합격'
    
    df['합격여부'] = [ "합격" if n >= 20 else "불합격" for n in df['평균']]
    ```
    
- **df['컬럼명'] = Series**
    
    ```python
    df["과학"]=pd.Series(data=[10,20,30,40], index=[1,2,3,4])
    print(df)
    '''
       이름  국어  수학  영어  과학
    1  홍길동  30  20  10  10
    2  이순신  26  12  20  20
    3  유관순  11  20  30  30
    4  강감찬  10  12  40  40
    '''
    ```
    
    <aside>
    💡 pd.Series() 는 인덱스를 0부터 가져가기 때문에
    pd.Series() 사용할 때에는 인덱스 꼭 지정해야 한다.
    
    </aside>
    

### new_df = df.assign(컬럼명=리스트 | 함수)

- **new_df = df.assign(컬럼명=리스트)**
    
    ```python
    # 원본 데이터
    
    df = pd.DataFrame({"이름":['홍길동','이순신','유관순','강감찬'],
                       "국어":[30, 26, 11, 10],
                       "수학":[20, 12, 20, 12]
                     }, index=[1,2,3,4])
    
    '''
        이름  국어  수학
    1  홍길동  30  20
    2  이순신  26  12
    3  유관순  11  20
    4  강감찬  10  12
    '''
    ```
    
    ```python
    # 영어 컬럼 추가
    
    new_df = df.assign(영어=[10,20,30,40])
    print(new_df)
    ```
    
- **new_df = df.assign(컬럼명=함수, 컬럼명=함수)**
    
    ```python
    # def 함수로 총합 만들기
    
    def total(x):
        return x['국어']+x['수학']+x['영어']
    ```
    
    ```python
    # lambda 함수로 적용하기
    
    df= df.assign(총합=lambda x :x['국어']+x['수학']+x['영어'])
    ```
    
    ```python
    # lambda 함수 적용하여 평균 컬럼 추가하기
    
    df = df.assign(평균=lambda x : x['총합']/3)
    df['평균'] = df['평균'].astype(np.int32)
    ```
    

### new_df = pd.concat([df,df2], axis=1)

```python
# 원본 데이터(df1, df2)

df = pd.DataFrame({"이름":['홍길동','이순신','유관순','강감찬'],
                   "국어":[30, 26, 11, 10],
                   "수학":[20, 12, 20, 12]
                 }, index=[1,2,3,4])

'''
    이름  국어  수학
1  홍길동  30  20
2  이순신  26  12
3  유관순  11  20
4  강감찬  10  12
'''

df2 = pd.DataFrame({"영어":[30, 26, 11, 10],
                   "과학":[20, 12, 20, 12]}, index=[1,2,3,4])

print(df2)
'''
   영어  과학
1  30  20
2  26  12
3  11  20
4  10  12
'''
```

```python
new_df = pd.concat([df,df2], axis=1)
print(new_df)
'''
    이름  국어  수학  영어  과학
1  홍길동  30  20  30  20
2  이순신  26  12  26  12
3  유관순  11  20  11  20
4  강감찬  10  12  10  12
'''
```

## 컬럼 삽입(원하는 위치에)

```python
# 원본 데이터

df = pd.DataFrame({"이름":['홍길동','이순신','유관순','강감찬'],
                   "국어":[30, 26, 11, 10],
                   "수학":[20, 12, 20, 12]
                 }, index=[1,2,3,4])

'''
    이름  국어  수학
1  홍길동  30  20
2  이순신  26  12
3  유관순  11  20
4  강감찬  10  12
'''
```

```python
# df.insert(idx(삽입할 위치), 컬럼명, 값)

df.insert(1,"영어",[30,26,11,10])
print(df)
'''
이름  영어  국어  수학
1  홍길동  30  30  20
2  이순신  26  26  12
3  유관순  11  11  20
4  강감찬  10  10  12
'''
```

## 컬럼 삭제

### 단일 컬럼 삭제

```python
# 원본 데이터

df = pd.DataFrame({"이름":['홍길동','이순신','유관순','강감찬'],
                   "국어":[30, 26, 11, 10],
                   "수학":[20, 12, 20, 12],
                   "영어":[30, 26, 11, 10],
                   "과학":[20, 12, 20, 12],
                   "체육":[30, 26, 11, 10],
                   "보건":[20, 12, 20, 12],
                   "화학":[30, 26, 11, 10],
                   "수리":[20, 12, 20, 12]
                 }, index=[1,2,3,4])

print(df)

'''
    이름  국어  수학  영어  과학  체육  보건  화학  수리
1  홍길동  30  20  30  20  30  20  30  20
2  이순신  26  12  26  12  26  12  26  12
3  유관순  11  20  11  20  11  20  11  20
4  강감찬  10  12  10  12  10  12  10  1
'''
```

- **df.pop(컬럼명)**
    
    ```python
    df.pop("국어")
    print(df)
    '''
        이름  수학  영어  과학  체육  보건  화학  수리
    1  홍길동  20  30  20  30  20  30  20
    2  이순신  12  26  12  26  12  26  12
    3  유관순  20  11  20  11  20  11  20
    4  강감찬  12  10  12  10  12  10  12
    '''
    ```
    
- **del df[컬럼명]**
    
    ```python
    del df['수학']
    print(df)
    '''
        이름  영어  과학  체육  보건  화학  수리
    1  홍길동  30  20  30  20  30  20
    2  이순신  26  12  26  12  26  12
    3  유관순  11  20  11  20  11  20
    4  강감찬  10  12  10  12  10  12
    '''
    ```
    

### 다중 컬럼 삭제

- **df.drop(columns=리스트)**
    
    ```python
    df.drop(columns=['영어', '과학'], inplace=True)
    print(df)
    
    '''
        이름  체육  보건  화학  수리
    1  홍길동  30  20  30  20
    2  이순신  26  12  26  12
    3  유관순  11  20  11  20
    4  강감찬  10  12  10  12
    '''
    ```
    
    ```python
    df.drop(columns=['체육', '보건'], inplace=True, axis=1)
    print(df)
    '''
        이름  화학  수리
    1  홍길동  30  20
    2  이순신  26  12
    3  유관순  11  20
    4  강감찬  10  12
    '''
    ```
    

## 행 추가

```python
# 원본 데이터(df1, df2)

info={"Name":["유관순","안중근"],"age":[18,31],"birthday":['1920/09/28','1910/03/26']}
df = pd.DataFrame(info)
print(df)
'''
   Name    age   birthday
0  유관순   18  1920/09/28
1  안중근   31  1910/03/26
'''

info2 = {"Name":["홍길동","강감찬"],"age":[22,43],"birthday":['1990/09/28','1980/03/26']}
df2 = pd.DataFrame(info2)
print(df2)
'''
  Name  age    birthday
0  홍길동   22  1990/09/28
1  강감찬   43  1980/03/26
'''
```

```python
new_df = pd.concat([df, df2],axis=0, ignore_index=True)

print(new_df)
'''
  Name  age    birthday
0  유관순   18  1920/09/28
1  안중근   31  1910/03/26
2  홍길동   22  1990/09/28
3  강감찬   43  1980/03/26
'''
```

<aside>
💡 한꺼번에 여러개의 DataFrame을 지정하여  행을 추가할 수 있다.
ignore_index=True를 통해 index가 꼬이지 않도록 한다.

</aside>

## 행 삭제

### new_df = df.drop(index=[인덱스명(라벨), 인덱스명])

```python
# 원본 데이터

df = pd.DataFrame({"이름":['홍길동','이순신','유관순','강감찬'],
                   "국어":[30, 26, 11, 10],
                   "수학":[20, 12, 20, 12]
                 }, index=[1,2,3,4])

'''
    이름  국어  수학
1  홍길동  30  20
2  이순신  26  12
3  유관순  11  20
4  강감찬  10  12
'''
```

```python
df.drop(index=[1,2],inplace=True)
print(df)

'''
	이름  국어  수학
3  유관순  11  20
4  강감찬  10  12
'''
```

### new_df = df.drop([인덱스명, 인덱스명(라벨)], axis=0)

```python
df.drop([3],inplace=True, axis=0)
print(df)
'''
이름  국어  수학
4  강감찬  10  12
'''
```

<aside>
💡 ‘index=’로 지정 안해줄 경우 axis=0을 명시해야 함.

</aside>

## null 조회 / 삭제 / 치환

### null 조회

> **null 값 조회 : None, NaN or NA as null**

**1) Pandas 함수 이용**
  - bool = pd.isna( 스칼라 | Series | df )
  - bool = pd.isnull( 스칼라 | Series | df )
  - bool = pd.notnull( 스칼라 | Series | df )

**2) DataFrame 함수 이용**
  - bool = df.isnul( )
  - bool = df[컬럼명].isnull( )
  - bool = df[컬럼, 컬럼2].isnull( )
> 

```python
# 원본 데이터

df = pd.DataFrame({ "col1" : [1 ,1, 1, None, 1],
                    "col2" : [2, 2, 2, 2, np.nan],
                    "col3" : [ np.nan, 3, 3, 3, 3],
                    "col4" : [ np.nan, np.nan, np.nan, np.nan, np.nan]},
                    index = [1, 2, 3, 4, 5])

print(df)

'''
   col1  col2  col3  col4
1   1.0   2.0   NaN   NaN
2   1.0   2.0   3.0   NaN
3   1.0   2.0   3.0   NaN
4   NaN   2.0   3.0   NaN
5   1.0   NaN   3.0   NaN
'''
```

- **Pandas 함수**
    1. **전체 데이터프레임에 NaN값 있는지 확인**
        
        ```python
        print(pd.isna(df))
        print(pd.isnull(df))
        '''
            col1   col2   col3  col4
        1  False  False   True  True
        2  False  False  False  True
        3  False  False  False  True
        4   True  False  False  True
        5  False   True  False  True
        '''
        ```
        
        ```python
        # NaN이 아니면 True
        
        print(pd.notnull(df))
        print(~pd.isnull(df))
        '''
            col1   col2   col3   col4
        1   True   True  False  False
        2   True   True   True  False
        3   True   True   True  False
        4  False   True   True  False
        5   True  False   True  False
        '''
        ```
        
    2. **특정 Series에 NaN값 있는지 확인**
        
        ```python
        print(pd.isna(df['col1']))
        print(pd.isnull(df['col1']))
        '''
        1    False
        2    False
        3    False
        4     True
        5    False
        Name: col1, dtype: bool
        '''
        ```
        
    3. **특정 column들(DataFrame)에 NaN값 있는지 확**
        
        ```python
        print(pd.isna(df[['col1','col2']]))
        print(pd.isnull(df[['col1','col2']])) # fancy 처럼 대괄호 필요
        '''
            col1   col2
        1  False  False
        2  False  False
        3  False  False
        4   True  False
        5  False   True
        '''
        ```
        
- **DataFrame 함수**
    1. **전체 데이터프레임에 NaN값 있는지 확인**
        
        ```python
        print(df.isnull())
        print(df.isna())
        
        '''
            col1   col2   col3  col4
        1  False  False   True  True
        2  False  False  False  True
        3  False  False  False  True
        4   True  False  False  True
        5  False   True  False  True
        '''
        ```
        
    2. **특정 Series에 NaN값 있는지 확인**
        
        ```python
        print(df['col1'].isnull())
        '''
        1    False
        2    False
        3    False
        4     True
        5    False
        Name: col1, dtype: bool
        '''
        ```
        
    3. **특정 column들(DataFrame)에 NaN값 있는지 확인**
        
        ```python
        print(df[['col1','col2']].isnull())
        '''
            col1   col2
        1  False  False
        2  False  False
        3  False  False
        4   True  False
        5  False   True
        '''
        ```
        

### null 삭제

- **null이 있는 행 삭제**
    
    ```python
    # 원본 데이터
    
    df = pd.DataFrame({"col1": [1, 1, 1, 1, np.nan],
                       "col2": [2, 2, 2, 2, np.nan],
                       "col3": [3, np.nan, np.nan, np.nan, np.nan],
                       "col4": [2, np.nan, np.nan, np.nan, np.nan]},
                      index=[1, 2, 3, 4, 5])
    
    print(df)
    '''
       col1  col2  col3  col4
    1   1.0   2.0   3.0   2.0
    2   1.0   2.0   NaN   NaN
    3   1.0   2.0   NaN   NaN
    4   1.0   2.0   NaN   NaN
    5   NaN   NaN   NaN   NaN
    '''
    ```
    
    1. **new_df = df.dropna( axis=0|'index', inplace=False )**
        
        ```python
        new_df = df.dropna(axis=0)
        print(new_df)
        '''
           col1  col2  col3  col4
        1     1   2.0   3.0   2.0
        '''
        
        # NaN값이 있는 2~5행이 모두 삭제됨
        ```
        
    2. **new_df = df.dropna( axis=0|'index', how="any|all" , inplace=False)**
        
        ```python
        # how=any
        # NaN값이 하나라도 있는 행 삭제 => 2~5행 삭제
        
        new_df = df.dropna(axis=0, how='any')
        print(new_df)
        '''
        col1  col2  col3  col4
        1   1.0   2.0   3.0   2.0
        '''
        ```
        
        ```python
        # how=all
        # 행의 모든 값이 NaN인 행 삭제 => 5행 삭
        
        new_df = df.dropna(axis=0, how='all')
        print(new_df)
        
        '''
        col1  col2  col3  col4
        1   1.0   2.0   3.0   2.0
        2   1.0   2.0   NaN   NaN
        3   1.0   2.0   NaN   NaN
        4   1.0   2.0   NaN   NaN
        '''
        ```
        
- **null이 있는 열 삭제**
    
    ```python
    # 원본 데이터
    
    df = pd.DataFrame({"col1": [1, 1, 1, 1, np.nan],
                       "col2": [2, 2, 2, 2, np.nan],
                       "col3": [3, np.nan, np.nan, np.nan, np.nan],
                       "col4": [np.nan, np.nan, np.nan, np.nan, np.nan]},
                      index=[1, 2, 3, 4, 5])
    
    print(df)
    '''
       col1  col2  col3  col4
    1   1.0   2.0   3.0   NaN
    2   1.0   2.0   NaN   NaN
    3   1.0   2.0   NaN   NaN
    4   1.0   2.0   NaN   NaN
    5   NaN   NaN   NaN   NaN
    '''
    ```
    
    1. **new_df = df.dropna( axis=1|'column', inplace=False )**
        
        ```python
        new_df = df.dropna(axis=1)
        print(new_df)
        '''
        Empty DataFrame
        Columns: []
        Index: [1, 2, 3, 4, 5]
        '''
        
        # NaN값이 있는 col1~col4가 모두 삭제됨
        ```
        
    2. **new_df = df.dropna( axis=1|'column', how="any|all" , inplace=False )**
        
        ```python
        # how=any
        # NaN값이 하나라도 있는 컬럼 삭제 => 모든 컬럼 삭제
        
        new_df = df.dropna(axis=1, how='any')
        print(new_df)
        '''
        Empty DataFrame
        Columns: []
        Index: [1, 2, 3, 4, 5]
        '''
        ```
        
        ```python
        # how=all
        # 컬럼의 모든 값이 NaN인 컬럼 삭제 => col4 삭
        
        new_df = df.dropna(axis=1, how='all')
        print(new_df)
        '''
           col1  col2  col3
        1   1.0   2.0   3.0
        2   1.0   2.0   NaN
        3   1.0   2.0   NaN
        4   1.0   2.0   NaN
        5   NaN   NaN   NaN
        '''
        ```
        

### null 치환

```python
# 원본 데이터

df = pd.DataFrame({"col1": [1, 1, 1, 1, np.nan],
                   "col2": [2, 2, 2, 2, np.nan],
                   "col3": [3, 3, 3, 3, np.nan],
                   "col4": [np.nan, np.nan, np.nan, np.nan, np.nan]},
                  index=[1, 2, 3, 4, 5])

print(df)
'''
   col1  col2  col3  col4
1   1.0   2.0   3.0   NaN
2   1.0   2.0   3.0   NaN
3   1.0   2.0   3.0   NaN
4   1.0   2.0   3.0   NaN
5   NaN   NaN   NaN   NaN
'''
```

- **전체 데이터프레임의 null값을 임의의 값으로 치환**
    
    ⇒ 일반적으로는 평균값을 사용한다.
    
    ```python
    # 0으로 치환하기
    
    new_df = df.fillna(0)
    print(new_df)
    '''
       col1  col2  col3  col4
    1   1.0   2.0   3.0   0.0
    2   1.0   2.0   3.0   0.0
    3   1.0   2.0   3.0   0.0
    4   1.0   2.0   3.0   0.0
    5   0.0   0.0   0.0   0.0
    '''
    ```
    
- **column마다 다르게 null값을 임의의 값으로 변경**
    
    ```python
    new_df = df.fillna({'col1':-1, 'col2':-2})
    print(new_df)
    '''
       col1  col2  col3  col4
    1   1.0   2.0   3.0   NaN
    2   1.0   2.0   3.0   NaN
    3   1.0   2.0   3.0   NaN
    4   1.0   2.0   3.0   NaN
    5  -1.0  -2.0   NaN   NaN
    '''
    ```
    
- **null값의 앞에 있는 값으로 변경**
    
    ```python
    # 원본 데이터
    
    df = pd.DataFrame({ "col1" : [1 ,np.nan, 3, 4, np.nan],
                        "col2" : [1 ,np.nan, 3, 4, np.nan],
                        "col3" : [1 ,2, np.nan, 4, np.nan]},
                        index = [1, 2, 3, 4, 5])
    
    print(df)
    '''
       col1  col2  col3
    1   1.0   1.0   1.0
    2   NaN   NaN   2.0
    3   3.0   3.0   NaN
    4   4.0   4.0   4.0
    5   NaN   NaN   NaN
    '''
    ```
    
    ```python
    new_df = df.fillna(method='ffill')
    print(new_df)
    '''
       col1  col2  col3
    1   1.0   1.0   1.0
    2   1.0   1.0   2.0
    3   3.0   3.0   2.0
    4   4.0   4.0   4.0
    5   4.0   4.0   4.0
    '''
    ```
    
- **null값의 뒤에 있는 값으로 변경**
    
    ```python
    new_df = df.fillna(method='bfill')
    print(new_df)
    '''
       col1  col2  col3
    1   1.0   1.0   1.0
    2   3.0   3.0   2.0
    3   3.0   3.0   4.0
    4   4.0   4.0   4.0
    5   NaN   NaN   NaN
    '''
    ```
    

## 정렬

### 값으로 정렬

```python
# 원본 데이터 만들기

import seaborn as sns

df = sns.load_dataset("mpg")
print("1. DataFrame")
df = df.head(10) # 행 개수 지정안해주면 기본으로 5개까지 보여줌
df.index=list('HDAFCBEGIJ')
print(df, df.shape)
'''
		mpg  cylinders  displacement  ...  model_year  origin                       name
H  18.0          8         307.0  ...          70     usa  chevrolet chevelle malibu
D  15.0          8         350.0  ...          70     usa          buick skylark 320
A  18.0          8         318.0  ...          70     usa         plymouth satellite
F  16.0          8         304.0  ...          70     usa              amc rebel sst
C  17.0          8         302.0  ...          70     usa                ford torino
B  15.0          8         429.0  ...          70     usa           ford galaxie 500
E  14.0          8         454.0  ...          70     usa           chevrolet impala
G  14.0          8         440.0  ...          70     usa          plymouth fury iii
I  14.0          8         455.0  ...          70     usa           pontiac catalina
J  15.0          8         390.0  ...          70     usa         amc ambassador dpl
'''

# null값 만들기
df[df['name']=='ford torino']=np.nan
print(df, df.shape)
'''
		mpg  cylinders  displacement  ...  model_year  origin                      name
H  18.0        8.0         307.0  ...        70.0     usa  chevrolet chevelle malibu
D  15.0        8.0         350.0  ...        70.0     usa          buick skylark 320
A  18.0        8.0         318.0  ...        70.0     usa         plymouth satellite
F  16.0        8.0         304.0  ...        70.0     usa              amc rebel sst
C   NaN        NaN           NaN  ...         NaN     NaN                        NaN
B  15.0        8.0         429.0  ...        70.0     usa           ford galaxie 500
E  14.0        8.0         454.0  ...        70.0     usa           chevrolet impala
G  14.0        8.0         440.0  ...        70.0     usa          plymouth fury iii
I  14.0        8.0         455.0  ...        70.0     usa           pontiac catalina
J  15.0        8.0         390.0  ...        70.0     usa         amc ambassador dpl
'''
```

- **mpg 컬럼 기준 오름차순 정렬**
    
    ```python
    new_df = df.sort_values(by='mpg',ascending=False, inplace=False, na_position='first')
    print(new_df)
    '''
    		mpg  cylinders  displacement  ...  model_year  origin                       name
    C   NaN        NaN           NaN  ...         NaN     NaN                        NaN
    H  18.0        8.0         307.0  ...        70.0     usa  chevrolet chevelle malibu
    A  18.0        8.0         318.0  ...        70.0     usa         plymouth satellite
    F  16.0        8.0         304.0  ...        70.0     usa              amc rebel sst
    D  15.0        8.0         350.0  ...        70.0     usa          buick skylark 320
    B  15.0        8.0         429.0  ...        70.0     usa           ford galaxie 500
    J  15.0        8.0         390.0  ...        70.0     usa         amc ambassador dpl
    E  14.0        8.0         454.0  ...        70.0     usa           chevrolet impala
    G  14.0        8.0         440.0  ...        70.0     usa          plymouth fury iii
    I  14.0        8.0         455.0  ...        70.0     usa           pontiac catalina
    '''
    
    ## ascending=False : 내림차순
    ## na_position='first' : NaN 값이 맨 위로 오도록
    ```
    
- **다중 정렬**
    - mpg 컬럼 기준 오름차순 정렬 + displacement 기준으로 한번 더 정렬
    
    ```python
    new_df = df.sort_values(by=['mpg','displacement'],ascending=True, inplace=False, na_position='first')
    print(new_df)
    '''
    		mpg  cylinders  displacement  ...  model_year  origin                       name
    C   NaN        NaN           NaN  ...         NaN     NaN                        NaN
    G  14.0        8.0         440.0  ...        70.0     usa          plymouth fury iii
    E  14.0        8.0         454.0  ...        70.0     usa           chevrolet impala
    I  14.0        8.0         455.0  ...        70.0     usa           pontiac catalina
    D  15.0        8.0         350.0  ...        70.0     usa          buick skylark 320
    J  15.0        8.0         390.0  ...        70.0     usa         amc ambassador dpl
    B  15.0        8.0         429.0  ...        70.0     usa           ford galaxie 500
    F  16.0        8.0         304.0  ...        70.0     usa              amc rebel sst
    H  18.0        8.0         307.0  ...        70.0     usa  chevrolet chevelle malibu
    A  18.0        8.0         318.0  ...        70.0     usa         plymouth satellite
    
    [10 rows x 9 columns]
    '''
    
    ```
    

### 행 라벨(index) 및 컬럼 라벨(컬럼명) 정렬

```python
# 원본 데이터

import seaborn as sns
df = sns.load_dataset("mpg")
print("1. DataFrame")
df = df.head(10) # 행 개수 지정안해주면 기본으로 5개까지 보여줌
df.index=list('HDAFCBEGIJ')
print(df, df.shape)
'''
		mpg  cylinders  displacement  ...  model_year  origin                       name
H  18.0          8         307.0  ...          70     usa  chevrolet chevelle malibu
D  15.0          8         350.0  ...          70     usa          buick skylark 320
A  18.0          8         318.0  ...          70     usa         plymouth satellite
F  16.0          8         304.0  ...          70     usa              amc rebel sst
C  17.0          8         302.0  ...          70     usa                ford torino
B  15.0          8         429.0  ...          70     usa           ford galaxie 500
E  14.0          8         454.0  ...          70     usa           chevrolet impala
G  14.0          8         440.0  ...          70     usa          plymouth fury iii
I  14.0          8         455.0  ...          70     usa           pontiac catalina
J  15.0          8         390.0  ...          70     usa         amc ambassador dpl
'''
```

- **행단위(행라벨) 정렬**
    
    ```python
    new_df = df.sort_index(axis=0)
    new_df = df.sort_index(axis=0, ascending=False)
    #new_df = df.sort_index(axis=0, ascending=False, na_position='first')
    print(new_df)
    '''
    		mpg  cylinders  displacement  ...  model_year  origin                       name
    J  15.0          8         390.0  ...          70     usa         amc ambassador dpl
    I  14.0          8         455.0  ...          70     usa           pontiac catalina
    H  18.0          8         307.0  ...          70     usa  chevrolet chevelle malibu
    G  14.0          8         440.0  ...          70     usa          plymouth fury iii
    F  16.0          8         304.0  ...          70     usa              amc rebel sst
    E  14.0          8         454.0  ...          70     usa           chevrolet impala
    D  15.0          8         350.0  ...          70     usa          buick skylark 320
    C  17.0          8         302.0  ...          70     usa                ford torino
    B  15.0          8         429.0  ...          70     usa           ford galaxie 500
    A  18.0          8         318.0  ...          70     usa         plymouth satellite
    '''
    ```
    
- **열단위(컬럼명) 정렬**
    
    ```python
    new_df = df.sort_index(axis=1, ascending=False)
    print(new_df)
    '''
    		weight origin  ... cylinders  acceleration
    H    3504    usa  ...         8          12.0
    D    3693    usa  ...         8          11.5
    A    3436    usa  ...         8          11.0
    F    3433    usa  ...         8          12.0
    C    3449    usa  ...         8          10.5
    B    4341    usa  ...         8          10.0
    E    4354    usa  ...         8           9.0
    G    4312    usa  ...         8           8.5
    I    4425    usa  ...         8          10.0
    J    3850    usa  ...         8           8.5
    '''
    ```
    

## DataFrame 함수

### 기술통계 관련 함수

- **최대 / 최소값 구하기**
    1. **행을 축으로 최대 / 최소값 구하기 (컬럼별 : 위 → 아래 비교)**
        
        ```python
        # 원본 데이터
        
        df = pd.DataFrame({"col1" : [4 ,6, 9, 5, 15],
                           "col2" : [16, 8, np.nan, 6, 6],
                           "col3" : [10, 11, 12, 12, 12]},
                            index = list("ABCDE"))
        print(df)
        '''
           col1  col2  col3
        A     4  16.0    10
        B     6   8.0    11
        C     9   NaN    12
        D     5   6.0    12
        E    15   6.0    12
        '''
        ```
        
        ```python
        x = df.max(axis=0)
        print(x)
        '''
        col1    15.0
        col2    16.0
        col3    12.0
        dtype: float64
        '''
        x = df.min(axis=0)
        print(x)
        '''
        col1     4.0
        col2     6.0
        col3    10.0
        dtype: float64
        '''
        ```
        
    2. **열을 축으로 최대 / 최소값 구하기 (행별 : 왼→오)**
        
        ```python
        x = df.max(axis=1)
        print(x)
        '''
        A    16.0
        B    11.0
        C    12.0
        D    12.0
        E    15.0
        dtype: float64
        '''
        x = df.min(axis=1)
        print(x)
        '''
        A    4.0
        B    6.0
        C    9.0
        D    5.0
        E    6.0
        dtype: float64
        '''
        ```
        
- **누적 최대 / 최소값 구하기**
    1. **행을 축으로 누적 최대 / 최소값 구하기 (컬럼별 : 위 → 아래)**
        
        ```python
        # 원본 데이터
        '''
           col1  col2  col3
        A     4  16.0    10
        B     6   8.0    11
        C     9   NaN    12
        D     5   6.0    12
        E    15   6.0    12
        '''
        
        # 누적 최대값
        x = df.cummax(axis=0)
        print(x)
        '''
           col1  col2  col3
        A     4  16.0    10
        B     6  16.0    11
        C     9   NaN    12
        D     9  16.0    12
        E    15  16.0    12
        '''
        
        # 누적 최소값
        x = df.cummin(axis=0)
        print(x)
        '''
           col1  col2  col3
        A     4  16.0    10
        B     4   8.0    10
        C     4   NaN    10
        D     4   6.0    10
        E     4   6.0    10
        '''
        ```
        
    2. **열을 축으로 누적 최대 / 최소값 구하기 (행별 : 왼 → 오)**
        
        ```python
        # 원본 데이터
        '''
           col1  col2  col3
        A     4  16.0    10
        B     6   8.0    11
        C     9   NaN    12
        D     5   6.0    12
        E    15   6.0    12
        '''
        
        # 누적 최대값
        x = df.cummax(axis=1)
        print(x)
        '''
           col1  col2  col3
        A   4.0  16.0  16.0
        B   6.0   8.0  11.0
        C   9.0   NaN  12.0
        D   5.0   6.0  12.0
        E  15.0  15.0  15.0
        '''
        
        # 누적 최소값
        x = df.cummin(axis=1)
        print(x)
        '''
           col1  col2  col3
        A   4.0   4.0   4.0
        B   6.0   6.0   6.0
        C   9.0   NaN   9.0
        D   5.0   5.0   5.0
        E  15.0   6.0   6.0
        '''
        ```
        
- **최대 / 최소값 label 구하기**
    1. **행을 축으로 최대 / 최소값의 라벨(인덱스) 구하기 (위 → 아래)**
        
        ```python
        # 원본 데이터
        '''
           col1  col2  col3
        A     4  16.0    10
        B     6   8.0    11
        C     9   NaN    12
        D     5   6.0    12
        E    15   6.0    12
        '''
        
        # 컬럼별 최대값을 가진 라벨 구하기
        x = df.idxmax(axis=0)
        print(x)
        '''
        col1    E
        col2    A
        col3    C
        dtype: object
        '''
        
        # 컬럼별 최소값을 가진 라벨 구하기
        x = df.idxmin(axis=0)
        print(x)
        '''
        col1    A
        col2    D
        col3    A
        dtype: object
        '''
        ```
        
    2. **열을 축으로 최대 / 최소값 라벨(컬럼명) 구하기**
        
        ```python
        # 원본 데이터
        '''
           col1  col2  col3
        A     4  16.0    10
        B     6   8.0    11
        C     9   NaN    12
        D     5   6.0    12
        E    15   6.0    12
        '''
        
        # 행별 최대값을 가진 컬럼명 구하기
        x = df.idxmax(axis=1)
        print(x)
        '''
        A    col2
        B    col3
        C    col3
        D    col3
        E    col1
        dtype: object
        '''
        
        # 행별 최소값을 가진 컬럼명 구하기
        x = df.idxmin(axis=1)
        print(x)
        '''
        A    col1
        B    col1
        C    col1
        D    col1
        E    col2
        dtype: object
        '''
        ```
        
- **총합 구하기**
    1. **행을 축으로 총합 / 누적 총합 구하기 (컬럼별)**
        
        ```python
        # 원본 데이터
        '''
           col1  col2  col3
        A     4  16.0    10
        B     6   8.0    11
        C     9   NaN    12
        D     5   6.0    12
        E    15   6.0    12
        '''
        
        # 컬럼별 총합 구하기
        x = df.sum(axis=0)
        print(x)
        '''
        col1    39.0
        col2    36.0
        col3    57.0
        dtype: float64
        '''
        
        # 컬럼별 누적 총합 구하기
        x = df.cumsum(axis=0) # 중요***
        print(x)
        '''
           col1  col2  col3
        A     4  16.0    10
        B    10  24.0    21
        C    19   NaN    33
        D    24  30.0    45
        E    39  36.0    57
        '''
        ```
        
    2. **열을 축으로 총합 / 누적 총합 구하기 (행별)**
        
        ```python
        # 원본 데이터
        '''
           col1  col2  col3
        A     4  16.0    10
        B     6   8.0    11
        C     9   NaN    12
        D     5   6.0    12
        E    15
        '''
        
        # 행별 총합 구하기
        x = df.sum(axis=1)
        print(x)
        '''
        A    30.0
        B    25.0
        C    21.0
        D    23.0
        E    33.0
        dtype: float64
        '''
        
        # 행별 누적 총합 구하기
        x = df.cumsum(axis=1) # 중요***
        print(x)
        '''
           col1  col2  col3
        A   4.0  20.0  30.0
        B   6.0  14.0  25.0
        C   9.0   NaN  21.0
        D   5.0  11.0  23.0
        E  15.0  21.0  33.0
        '''
        ```
        
- **평균 구하기**
    1. **행을 축으로 평균 구하기**
        
        ```python
        # 원본 데이터
        '''
           col1  col2  col3
        A     4  16.0    10
        B     6   8.0    11
        C     9   NaN    12
        D     5   6.0    12
        E    15   6.0    12
        '''
        
        # 컬럼별 평균 구하기
        x = df.mean(axis=0)
        print(x)
        '''
        col1     7.8
        col2     9.0
        col3    11.4
        dtype: float64
        '''
        ```
        
    2. **열을 축으로 평균 구하기**
        
        ```python
        # 원본 데이터
        '''
           col1  col2  col3
        A     4  16.0    10
        B     6   8.0    11
        C     9   NaN    12
        D     5   6.0    12
        E    15   6.0    12
        '''
        
        # 행별 평균 구하기
        x = df.mean(axis=1)
        print(x)
        '''
        A    10.000000
        B     8.333333
        C    10.500000
        D     7.666667
        E    11.000000
        dtype: float64
        '''
        ```
        
- **중앙값 구하기**
    1. **행을 축으로 중앙값 구하기 (컬럼별)**
        
        ```python
        # 원본 데이터
        '''
           col1  col2  col3
        A     4  16.0    10
        B     6   8.0    11
        C     9   NaN    12
        D     5   6.0    12
        E    15   6.0    12
        '''
        
        # 컬럼별 중앙값 구하기
        x = df.median(axis=0)
        print(x)
        '''
        col1     6.0
        col2     7.0
        col3    12.0
        dtype: float64
        '''
        ```
        
    2. **열을 축으로 중앙값 구하기 (행별)**
        
        ```python
        # 원본 데이터
        '''
           col1  col2  col3
        A     4  16.0    10
        B     6   8.0    11
        C     9   NaN    12
        D     5   6.0    12
        E    15   6.0    12
        '''
        
        # 행별 중앙값 구하기
        x = df.median(axis=1)
        print(x)
        '''
        A    10.0
        B     8.0
        C    10.5
        D     6.0
        E    12.0
        dtype: float64
        '''
        ```
        
- **곱연산 구하기**
    1. **행을 축으로 곱연산 구하기**
        
        ```python
        # 원본 데이터
        '''
           col1  col2  col3
        A     4  16.0    10
        B     6   8.0    11
        C     9   NaN    12
        D     5   6.0    12
        E    15   6.0    12
        '''
        
        x = df.prod(axis=0)
        print(x)
        '''
        col1     16200.0
        col2      4608.0
        col3    190080.0
        dtype: float64
        '''
        ```
        
    2. **열을 축으로 곱연산 구하기**
        
        ```python
        # 원본 데이터
        '''
           col1  col2  col3
        A     4  16.0    10
        B     6   8.0    11
        C     9   NaN    12
        D     5   6.0    12
        E    15   6.0    12
        '''
        
        x = df.prod(axis=1)
        print(x)
        '''
        A     640.0
        B     528.0
        C     108.0
        D     360.0
        E    1080.0
        dtype: float64
        '''
        ```
        
- **분산 구하기**
    
    ```python
    # 원본 데이터
    '''
       col1  col2  col3
    A     4  16.0    10
    B     6   8.0    11
    C     9   NaN    12
    D     5   6.0    12
    E    15   6.0    12
    '''
    
    x = df.var(axis=0)
    print(x)
    '''
    col1    19.700000
    col2    22.666667
    col3     0.800000
    dtype: float64
    '''
    x = df.var(axis=1)
    print(x)
    '''
    A    36.000000
    B     6.333333
    C     4.500000
    D    14.333333
    E    21.000000
    dtype: float64
    '''
    ```
    
- **표준편차 구하기**
    
    ```python
    x = df.std(axis=0)
    print(x)
    '''
    col1    4.438468
    col2    4.760952
    col3    0.894427
    dtype: float64
    '''
    x = df.std(axis=1)
    print(x)
    '''
    A    6.000000
    B    2.516611
    C    2.121320
    D    3.785939
    E    4.582576
    dtype: float64
    '''
    ```
    
- **개수 구하기 (null 제외)**
    
    ```python
    x = df.count(axis=0)
    print(x)
    '''
    col1    5
    col2    4
    col3    5
    dtype: int64
    '''
    x = df.count(axis=1)
    print(x)
    '''
    A    3
    B    3
    C    2
    D    3
    E    3
    dtype: int64
    '''
    ```
    
- **통합 통계 데이터**
    
    ```python
    x = df.describe()
    print(x)
    '''
                col1       col2       col3
    count   5.000000   4.000000   5.000000
    mean    7.800000   9.000000  11.400000
    std     4.438468   4.760952   0.894427
    min     4.000000   6.000000  10.000000
    25%     5.000000   6.000000  11.000000
    50%     6.000000   7.000000  12.000000
    75%     9.000000  10.000000  12.000000
    max    15.000000  16.000000  12.000000
    '''
    ```
    
    ```python
    x = df.info()
    print(x)
    '''
     #   Column  Non-Null Count  Dtype  
    ---  ------  --------------  -----  
     0   col1    5 non-null      int64  
     1   col2    4 non-null      float64
     2   col3    5 non-null      int64  
    dtypes: float64(1), int64(2)
    memory usage: 160.0+ bytes
    None
    '''
    ```
    

### 주요 함수