/// <reference types="node" />
import { AssetsMap } from '../utils/assets';
import { AssetType, OtherAssetType } from './misc';
import { RunnerOptions } from './runner';
import { FormatOptions } from './format';
export declare type FontGeneratorOptions = RunnerOptions & {
    assets: AssetsMap;
    formatOptions: FormatOptions;
    templates: {
        [key in OtherAssetType]: string;
    };
};
export declare type Result = Promise<string | Buffer>;
export declare type FontGeneratorFn<DependencyT> = (options: FontGeneratorOptions, dependencyContent: DependencyT extends {} ? DependencyT : null) => Result;
export declare type FontGenerator<DependencyT = void> = {
    generate: FontGeneratorFn<DependencyT>;
} & (DependencyT extends {} ? {
    dependsOn: AssetType;
} : {});
